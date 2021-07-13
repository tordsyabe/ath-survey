$(document).ready(function () {
  // Bootsrap select picker
  $(".selectpicker").selectpicker();

  var current_fs, next_fs, previous_fs; //fieldsets
  var opacity;

  $(".next").click(function (event) {
    event.preventDefault();
    current_fs = $(this).parent();
    next_fs = $(this).parent().next();

    //Add Class Active
    $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

    //show the next fieldset
    next_fs.show();
    //hide the current fieldset with style
    current_fs.animate(
      { opacity: 0 },
      {
        step: function (now) {
          // for making fielset appear animation
          opacity = 1 - now;

          current_fs.css({
            display: "none",
            position: "relative",
          });
          next_fs.css({ opacity: opacity });
        },
        duration: 600,
      }
    );
  });

  $(".previous").click(function (event) {
    event.preventDefault();
    current_fs = $(this).parent();
    previous_fs = $(this).parent().prev();

    //Remove class active
    $("#progressbar li")
      .eq($("fieldset").index(current_fs))
      .removeClass("active");

    //show the previous fieldset
    previous_fs.show();

    //hide the current fieldset with style
    current_fs.animate(
      { opacity: 0 },
      {
        step: function (now) {
          // for making fielset appear animation
          opacity = 1 - now;

          current_fs.css({
            display: "none",
            position: "relative",
          });
          previous_fs.css({ opacity: opacity });
        },
        duration: 600,
      }
    );
  });

  $(".radio-group .radio").click(function () {
    $(this).parent().find(".radio").removeClass("selected");
    $(this).addClass("selected");
  });

  $(".submit").click(function () {
    return false;
  });

  // onchange employees base on company
  $("#branch").on("change", function (event) {
    var comp_id = event.target.value;
    var staffSelection = $("#staff");

    console.log(comp_id);

    $.ajax({
      type: "GET",
      url: `/employees/${comp_id}`,
      contentType: "application/json",
      dataType: "json",
      success: function (data) {
        options = "";
        for (var i = 0; i < data.length; i++) {
          options += `<option value="${data[i].id}">${data[i].name}</option>`;
        }
        staffSelection.empty().append(options);
        staffSelection.selectpicker("refresh");
      },
      error: function (error) {
        console.log(error);
      },
    });
  });

  $(".clickable-row").on("click", function () {
    window.location = $(this).data("href");
  });
});
