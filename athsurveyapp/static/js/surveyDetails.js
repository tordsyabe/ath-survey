$(document).ready(function () {
  // survey table navigation
  $(".clickable-row").on("click", function () {
    window.location = $(this).data("href");
  });
  //   ADDING NEW SURVEY CATEGORY
  const surveyId = $("[data-surveyid]").data("surveyid");

  const saveSurveyCategoryForm = $("#surveyCategoryForm");

  saveSurveyCategoryForm.on("submit", function (event) {
    event.preventDefault();
    $("#saveCategorySpinner").css("display", "block");
    $("#saveCategorySpinner").addClass("d-inline-block");
    $("#saveSurveyCategoryBtn").prop("disabled", true);
    $("#saveSurveyCategoryBtn span").text("Saving");

    const categoryDescription = $(
      '#surveyCategoryForm input[id="qt_description"]'
    ).val();

    const categorySequence = $(
      '#surveyCategoryForm input[id="qt_sequence"]'
    ).val();

    $.ajax({
      type: "POST",
      url: "/api/question_types",
      contentType: "application/json",
      data: JSON.stringify({
        description: categoryDescription,
        survey_id: surveyId,
        sequence: categorySequence,
      }),

      success: function (data) {
        location.href = "/surveys/" + surveyId;
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
  // EDITING SURVEY NAME
  $("#surveyName").dblclick(function () {
    $(this).hide();
    const surveyNameInp = $(".survey-name-inline-input");

    surveyNameInp.show();
    surveyNameInp.focus();
    // const suveyNameInputWidth = 30 + $(this).width();
    // surveyNameInp.css({
    //   width: suveyNameInputWidth + "px",
    // });

    surveyNameInp.focusout(function () {
      $.ajax({
        type: "PUT",
        url: "/api/surveys/" + surveyId,
        contentType: "application/json",
        data: JSON.stringify({
          name: surveyNameInp.val(),
          description: $(".survey-description-inline-input").val(),
        }),
        success: function (data) {
          console.log(data);
          surveyNameInp.hide();
          surveyNameInp.prev().html(data.name);
          surveyNameInp.prev().show();
          toastr.success("Survey name updated successfully");
        },
        error: function (error) {
          toastr.error("There was an error updating survey name");
        },
      });
    });
  });

  // EDITING SURVEY DESCRIPTION
  $("#surveyDescription").dblclick(function () {
    $(this).hide();
    const surveyDescInp = $(".survey-description-inline-input");
    surveyDescInp.show();
    surveyDescInp.focus();
    // const suveyDescInputWidth = 30 + $(this).width();
    // surveyDescInp.css({
    //   width: suveyDescInputWidth + "px",
    // });
    surveyDescInp.focusout(function () {
      $.ajax({
        type: "PUT",
        url: "/api/surveys/" + surveyId,
        contentType: "application/json",
        data: JSON.stringify({
          name: $(".survey-name-inline-input").val(),
          description: surveyDescInp.val(),
        }),
        success: function (data) {
          console.log(data);
          surveyDescInp.hide();
          surveyDescInp.prev().html(data.description);
          surveyDescInp.prev().show();
          toastr.success("Survey description updated successfully");
        },
        error: function (error) {
          toastr.error("There was an error updating survey description");
        },
      });
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
        url: "/api/question_types/" + parseInt(categoryId),
        contentType: "application/json",
        data: JSON.stringify({
          description: categoryInput.val(),
          survey_id: surveyId,
          sequence: $(".survey-category-sq-inline-input").val(),
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
  // SETTING QUESTION ID TO DELETE
  $(".delete-question-form-modal-btn").on("click", function (e) {
    e.preventDefault();
    const questionIdToDel = $(this).parent().parent().data("questionid");
    console.log(questionIdToDel);
    $("#deleteQuestionForm").find("input:first").val(questionIdToDel);
  });
  // DELETE QUESTION
  $("#deleteQuestionForm").on("submit", function (e) {
    e.preventDefault();
    const dataQuestionId = $(this).find("input:first").val();
    $.ajax({
      type: "DELETE",
      url: "/api/questions/" + dataQuestionId,
      success: function (data) {
        location.href = "/surveys/" + surveyId;
      },
      error: function (error) {
        console.log(error);
      },
    });
  });

  //   SETTING CATEGORY ID TO DELETE
  $(".delete-category-form-modal-btn").on("click", function (e) {
    e.preventDefault();
    const categoryIdToDel = $(this).parent().parent().data("categoryid");
    console.log(categoryIdToDel);
    $("#deleteCategoryForm").find("input:first").val(categoryIdToDel);
  });

  //   DELETING SURVEY CATEGORY, SHOULD BE CASCADING WITH QUESTIONS
  $("#deleteCategoryForm").on("submit", function (e) {
    e.preventDefault();
    const dataCategoryId = $(this).find("input:first").val();

    $.ajax({
      type: "DELETE",
      url: "/api/question_types/" + dataCategoryId,
      success: function (data) {
        location.href = "/surveys/" + surveyId;
      },
      error: function (error) {
        console.log(error);
      },
    });
  });

  // ADD QUESTION BUTTON
  $(".add-question-btn").on("click", function (e) {
    const surveyCatDesc = $(this).siblings("h2").text();
    const surveyCatId = $(this).parent().parent().data("categoryid");
    $("#questionForm").trigger("reset");
    $("#questionForm").find("input[name='question_type_id']").val(surveyCatId);

    $(".question-description-form").html(`(${surveyCatDesc})`);
  });

  // SAVING QUESTION
  $("#questionForm").on("submit", function (e) {
    e.preventDefault();
    const q_id = $(this).find("input[name='q_id']").val();
    const desc = $(this).find("input[name='q_description']").val();
    const sq = $(this).find("input[name='q_sequence']").val();
    const choice = $(this).find("select[name='choice_id']").val();
    // const is_req = $(this).find("input[name='is_required']").val();
    const qt_id = $(this).find("input[name='question_type_id']").val();

    $.ajax({
      type: "POST",
      url: "/api/questions",
      contentType: "application/json",
      data: JSON.stringify({
        id: q_id,
        description: desc,
        sequence: parseInt(sq),
        is_required: true,
        question_type_id: parseInt(qt_id),
        choice_id: parseInt(choice),
      }),

      success: function (data) {
        console.log(data);
        location.href = "/surveys/" + surveyId;
      },
      error: function (error) {
        console.log(error);
      },
    });
  });

  $(".edit-question-form-modal-btn").on("click", function (e) {
    $("#questionFormModal").modal("toggle");
    const surveyCatDesc = $(this)
      .parent()
      .parent()
      .parent()
      .parent()
      .find("h2")
      .text();
    const surveyCatId = $(this)
      .parent()
      .parent()
      .parent()
      .parent()
      .parent()
      .data("categoryid");

    $("#questionForm").find("input[name='question_type_id']").val(surveyCatId);

    $(".question-description-form").html(`(${surveyCatDesc})`);
    const quesToEdit = $(this).parent().parent().data("questionid");
    const quesInfo = $(this).parent().parent();
    $('input[id="q_id"').val(quesToEdit);
    $('input[id="q_description"').val(
      $(quesInfo).find("td:eq(0) .font-weight-bold").text()
    );
    $('input[id="q_sequence"').val(
      $(quesInfo).find("td:eq(2) .font-weight-bold").text()
    );

    $('select[id="choice_id"').val(
      $(quesInfo).find("td:eq(1) span:first").text()
    );
  });
});
