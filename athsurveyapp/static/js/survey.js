$(document).ready(function () {
  $(".delete-survey-modal").on("click", function (e) {
    //   SETTING SURVEY TO DELETE
    e.preventDefault();
    e.stopPropagation();
    $("#deleteSurveyFormModal").modal("toggle");
    const surveyIdToDel = $(this).parent().parent().data("surveyid");

    $("#deleteSurveyForm").find("input:first").val(surveyIdToDel);
  });

  $("#deleteSurveyForm").on("submit", function (e) {
    e.preventDefault();
    const dataSurveyId = $(this).find("input:first").val();

    $.ajax({
      type: "DELETE",
      url: "/api/surveys/" + dataSurveyId,
      success: function (data) {
        location.href = "/surveys/";
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
});
