
if(!checkExist) {

  var checkExist = setInterval(function() {
     if ($('button.SasA11y-GTML-Launcher').length > 0) {
        // console.log("Exists! " + $('button.SasA11y-GTML-Launcher').length);
        $( "button.SasA11y-GTML-Launcher" ).each(function( index ) {
          // move button to top of chart
          // $( this ).appendTo("#accelerateButton");

          // change position
          $( this ).css(
                    { position: 'relative', 
                      top: '0px', 
                      left: '0px',
                      padding: '6px 12px',
                      'font-size': '14px'
                    });
          $( this ).addClass( "btn btn-info");

        });

        clearInterval(checkExist);

     } 
  }, 50);

};

// // move button to top of chart
// $("button.SasA11y-GTML-Launcher").appendTo("#accelerateButton");
// // change position
// $("button.SasA11y-GTML-Launcher").css(
//           { position: 'inherit', 
//             top: '0px', 
//             left: '0px',
//             padding: '6px 12px',
//             'font-size': '14px'
//           });
// $("button.SasA11y-GTML-Launcher").addClass( "btn btn-info");
// clearInterval(checkExist);

