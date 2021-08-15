$(document).ready(function () {
  const activePage = window.location.pathname;

  $(".nav-item").each(function () {
    var linkPage = $(this).find("a").attr("href");
    if (activePage === linkPage) {
      $(this).addClass("active");
    }
  });

  // Bootsrap select picker
  $(".selectpicker").selectpicker();

  var current_fs, next_fs, previous_fs; //fieldsets
  var opacity;

  $(".radio-group .radio").click(function () {
    $(this).parent().find(".radio").removeClass("selected");
    $(this).addClass("selected");
  });

  $(".submit").click(function () {
    return false;
  });
});
