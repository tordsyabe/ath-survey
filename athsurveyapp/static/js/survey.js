$(document).ready(function () {
  // survey table navigation
  $(".clickable-row").on("click", function () {
    window.location = $(this).data("href");
  });
  //   ADDING NEW SURVEY CATEGORY
  const surveryId = $("[data-surveyid]").data("surveyid");

  const saveSurveyCategoryBtn = $("#saveSurveyCategoryBtn");

  saveSurveyCategoryBtn.on("click", function (event) {
    const categoryDescription = $(
      '#surveyCategoryForm input[id="description"]'
    ).val();
    $.ajax({
      type: "POST",
      url: "/question_types/api",
      contentType: "application/json",
      data: JSON.stringify({
        description: categoryDescription,
        survey_id: surveryId,
      }),

      success: function (data) {
        location.href = "/surveys/" + surveryId;
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
  //   EDITING SURVEY CATEGORY
  $(".survey-category").dblclick(function () {
    $(this).hide();
    const categoryInput = $(this).next();
    categoryInput.show();
    categoryInput.focus();
    const inputWidth = 30 + $(this).width();
    categoryInput.css({
      width: inputWidth + "px",
    });
    categoryInput.focusout(function () {
      const categoryId = categoryInput.parent().parent().data("categoryid");

      console.log("out of focus", categoryInput.val(), categoryId);

      $.ajax({
        type: "PUT",
        url: "/question_types/api/" + parseInt(categoryId),
        contentType: "application/json",
        data: JSON.stringify({
          description: categoryInput.val(),
          survey_id: surveryId,
        }),
        success: function (data) {
          console.log(data);
          categoryInput.hide();
          categoryInput.prev().html(data.description);
          categoryInput.prev().show();
        },
        error: function (error) {
          console.log(error.responseJSON.message);
        },
      });
    });
  });
  //   SETTING CATEGORY ID TO DELETE
  $(".delete-category-form-modal-btn").on("click", function (e) {
    e.preventDefault();
    const categoryIdToDel = $(this).parent().data("categoryid");
    console.log(categoryIdToDel);
    $('#deleteCategoryForm input[id="id"]').val(categoryIdToDel);
  });

  //   DELETING SURVEY CATEGORY, SHOULD BE CASCADING WITH QUESTIONS
  $("#deleteCategoryForm").on("submit", function (e) {
    e.preventDefault();
    const dataCategoryId = $(this).find("input:first").val();
    $.ajax({
      type: "DELETE",
      url: "/question_types/api/" + dataCategoryId,
      success: function (data) {
        console.log(data);
        $("#deleteCategoryFormModal").modal("toggle");
        $(`div[data-categoryid=${dataCategoryId}]`).remove();
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
});
