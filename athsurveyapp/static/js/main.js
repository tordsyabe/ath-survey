$(document).ready(function () {
  // Bootsrap select picker
  $(".selectpicker").selectpicker();

  var current_fs, next_fs, previous_fs; //fieldsets
  var opacity;

  // $("#startSurveyBtn").click(function (event) {
  //   event.preventDefault();
  //   current_fs = $(this).parent();
  //   next_fs = $(this).parent().next();

  //   //show the next fieldset
  //   next_fs.show();
  //   //hide the current fieldset with style
  //   current_fs.animate(
  //     { opacity: 0 },
  //     {
  //       step: function (now) {
  //         // for making fielset appear animation
  //         opacity = 1 - now;

  //         current_fs.css({
  //           display: "none",
  //           position: "relative",
  //         });
  //         next_fs.css({ opacity: opacity });
  //       },
  //       duration: 600,
  //     }
  //   );
  // });

  // $(".previous").click(function (event) {
  //   event.preventDefault();
  //   current_fs = $(this).parent();
  //   previous_fs = $(this).parent().prev();

  //   //show the previous fieldset
  //   previous_fs.show();

  //   //hide the current fieldset with style
  //   current_fs.animate(
  //     { opacity: 0 },
  //     {
  //       step: function (now) {
  //         // for making fielset appear animation
  //         opacity = 1 - now;

  //         current_fs.css({
  //           display: "none",
  //           position: "relative",
  //         });
  //         previous_fs.css({ opacity: opacity });
  //       },
  //       duration: 600,
  //     }
  //   );
  // });

  $(".radio-group .radio").click(function () {
    $(this).parent().find(".radio").removeClass("selected");
    $(this).addClass("selected");
  });

  $(".submit").click(function () {
    return false;
  });
});
