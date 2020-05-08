(function() {
  // get all data in form and return object
  function getFormData(form) {
    var elements = form.elements;
    var honeypot;

    var fields = Object.keys(elements).filter(function(k) {
      if (elements[k].name === "honeypot") {
        honeypot = elements[k].value;
        return false;
      }
      return true;
    }).map(function(k) {
      if(elements[k].name !== undefined) {
        return elements[k].name;
      // special case for Edge's html collection
      }else if(elements[k].length > 0){
        return elements[k].item(0).name;
      }
    }).filter(function(item, pos, self) {
      return self.indexOf(item) == pos && item;
    });

    var formData = {};
    fields.forEach(function(name){
      var element = elements[name];

      // singular form elements just have one value
      formData[name] = element.value;

      // when our element has multiple items, get their values
      if (element.length) {
        var data = [];
        for (var i = 0; i < element.length; i++) {
          var item = element.item(i);
          if (item.checked || item.selected) {
            data.push(item.value);
          }
        }
        formData[name] = data.join(', ');
      }

    });

    // add form-specific values into the data
    formData.formDataNameOrder = JSON.stringify(fields);
    formData.formGoogleSheetName = form.dataset.sheet || "responses"; // default sheet name
    formData.formGoogleSendEmail
      = form.dataset.email || ""; // no email by default

    return {data: formData, honeypot: honeypot};
  }

  function handleFormSubmit(event) {  // handles form submit without any jquery
    event.preventDefault();           // we are submitting via xhr below
    var form = event.target;
    var formData = getFormData(form);
    var data = formData.data;

    if (!checkValidSubmission(formData)) {
      // console.log("bad submission");
      return false;
    }

    // If a honeypot field is filled, assume it was done so by a spam bot.
    if (formData.honeypot) {
      return false;
    }

    disableAllButtons(form);
    var url = form.action;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', url);
    // xhr.withCredentials = true;
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
          
          form.reset();
          
          var formElements = form.querySelector(".form-elements")
          if (formElements) {
            formElements.style.display = "none"; // hide form
          }
          
          // alert('Thank you for submitting a question. If you provided an email we will notify you of an answer. We will be posting Q&As in this website after May 10. In the meantime click below to browse Q&As others have submitted.');
          
          var thankYouMessage = form.querySelector(".thankyou_message");
          if (thankYouMessage) {
            thankYouMessage.style.display = "block";
          }
          
        }
    };
    // url encode form data for sending as post data
    var encoded = Object.keys(data).map(function(k) {
        return encodeURIComponent(k) + "=" + encodeURIComponent(data[k]);
    }).join('&');
    xhr.send(encoded);
  }

  function checkValidSubmission(formData) {

    // Question is required
    if (!formData.data.question) {
      return false;
    }

    // Modality is also required
    if (!formData.data.modality) {
      return false;
    }

    return true;
  
  }


  function handleFormSendComment(event) {  // handles form submit without any jquery


    event.preventDefault();           // we are submitting via xhr below
    var form = event.target;
    var formData = getFormData(form);
    var data = formData.data;

    if (!checkValidComment(formData)) {
      console.log("bad submission");
      return false;
    }

    disableSendButtons(form);

    console.log("here");
    
    var url = form.action;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', url);
    // xhr.withCredentials = true;
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
          
          form.reset();
          
          var formElements = form.querySelector(".form-elements")
          if (formElements) {
            formElements.style.display = "none"; // hide form
          }
          
          alert('We appreciate your feedback and comments.');
          
        }
    };
    // url encode form data for sending as post data
    var encoded = Object.keys(data).map(function(k) {
        return encodeURIComponent(k) + "=" + encodeURIComponent(data[k]);
    }).join('&');
    xhr.send(encoded);
    
  }

  function checkValidComment(formData) {

    // Question is required
    if (!formData.data.comment) {
      return false;
    }
    return true;
  
  }
  
  function loaded() {
    // bind to the submit event of our form
    var forms = document.querySelectorAll("form.gform");
    for (var i = 0; i < forms.length; i++) {
      forms[i].addEventListener("submit", handleFormSubmit, false);
    }

    var forms = document.querySelectorAll("form.gformComment");
    for (var i = 0; i < forms.length; i++) {
      forms[i].addEventListener("send", handleFormSendComment, false);
    }

  };

  document.addEventListener("DOMContentLoaded", loaded, false);

  function disableAllButtons(form) {
    var buttons = form.querySelectorAll("button");
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].disabled = true;
    }
  }

  function disableSendButtons(form) {
    var buttons = form.querySelectorAll("#commentButton");
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].disabled = true;
    }
  }

})();










