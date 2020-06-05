
window.onload = function(){

  var file = "Dataset/Q-A-Database - responses.csv";
  console.log(file);

  Papa.parse(file, {
      header: true,
      download: true,
      delimiter: ",",
      complete: function(results, file) {
          console.log("parsing complete");
          console.log(results.data);
          for (i = 0; i < results.data.length; i++) {
            // console.log(results.data[i].Timestamp);
            // console.log('{{page.title}}');
            if (results.data[i].post == "yes") {

              console.log("YES!");
              // post to Q&A
              // $("#menu").append('<li><a href="#">New list item</a></li>');

            }
          }
      }
  });

};