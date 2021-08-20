$(document).ready(function () {
  $("#saveResponseForm").submit(function () {
    $("#saveReponseSpinner").css("display", "block");
    $("#saveReponseSpinner").addClass("d-inline-block");
    $("#saveResponseBtn").prop("disabled", true);
    $("#saveResponseBtn span").text("Submitting");
  });

  let employee;
  const currentUsername = $(".user-name").eq(0).text();

  if (!$('select[id="branch"]').val()) {
    $("#startSurveyBtn").attr("disabled", true);
  }

  if (!$('select[id="employee"]').val()) {
    $("#startSurveyBtn").attr("disabled", true);
  }

  if (!$('select[id="survey"]').val()) {
    $("#startSurveyBtn").attr("disabled", true);
  }

  const params = get_query();
  $("#employee").selectpicker("val", params.employee);

  $('select[id="survey"]').change(function () {
    $("form")
      .children("fieldset")
      .each(function (index) {
        if (index > 0) {
          $(this).remove();
        }
      });

    $.ajax({
      type: "GET",
      url: `/api/surveys/${$(this).val()}`,
      contentType: "application/json",
      success: function (data) {
        let fieldsetCategory = "";
        const surveyName = data.name;
        $(".survey-name").html(data.name);

        for (let i = 0; i < data.question_types.length; i++) {
          let questions = "";

          data.question_types[i].questions.forEach((question) => {
            let choices = "";

            for (let k = 0; k < question.choice.value; k++) {
              choices += `
                        <input style="display: none;" class="form-check-input" type="radio" name="${
                          question.id
                        }" id="${question.description + k}" value="${k + 1}">
                        <label class="form-check-label" for="${
                          question.description + k
                        }">${k + 1}</label>
                        `;
            }

            questions += `
                    <tr>
                        <td class="w-50">
                            <label class="font-weight-bold">${
                              question.description
                            }</label>
                        </td>
                        <td>
                            <div class="form-check form-check-inline d-flex justify-content-between queston-choices">${choices}</div>
                            <div class="form-group py-3 mt-3" style="display: none;">
                                <input type="text" class="form-control" name="${
                                  question.id + ".feed"
                                }" placeholder="Please provide reason why less than 10">
                            </div>
                        </td>

                     </tr>

                    `;
          });

          fieldsetCategory += `
                <fieldset style="display: none;">
                <div class="row">
                    <div class="col-sm-auto col-md-6">
                        <p><span class="text-muted">Name:</span> <span class="font-weight-bold employee-name"></span></p>
                    </div>
                    <div class="col-sm-auto col-md-6">
                        <p><span class="text-muted">Branch:</span> <span class="font-weight-bold branch-name" ></span></p>
                    </div>
  
                    <div class="col-sm-auto col-md-6">
                        <p><span class="text-muted">Designation:</span> <span class="font-weight-bold employee-designation"></span></p>
                    </div>
                    <div class="col-sm-auto col-md-6">
                        <p><span class="text-muted">Survey:</span> <span class="font-weight-bold survey-name user-name">${surveyName}</span></p>
                    </div>
                    <div class="col-sm-auto col-md-6">
                        <p><span class="text-muted">Surveyor:</span> <span class="font-weight-bold">${currentUsername}</span></p>
                    </div>
                </div>

                <div class="row mt-5">
                    <div class="col-12">
                        <h3 class="font-weight-bold">${
                          data.question_types[i].description
                        }</h3>
    
                    
                    <div class="table-responsive-sm">
                    <table class="table my-5" id="tableSurvey">
                        <tbody>
                        ${questions}
                        </tbody>
                    </table>
                    </div>
                    </div>
                </div>

                <button class="btn btn-secondary previous font-weight-bold">Back</button>
                ${
                  data.question_types.length == i + 1
                    ? '<button type="submit" class="btn btn-info font-weight-bold">Submit</button>'
                    : '<button class="btn btn-info next font-weight-bold">Next</button>'
                }
            </fieldset>`;
        }

        $("form").append(fieldsetCategory);
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
  $('select[id="employee"]').on("change", function (e) {
    $("#startSurveyBtn").attr("disabled", false);
  });

  $('select[id="branch"]').on("change", function (e) {
    const branch_id = e.target.value;
    const empSelection = $('select[id="employee"]');
    $("#employeeSelectSpinner").css("display", "block");
    $.ajax({
      type: "GET",
      url: `/api/employees/branch/${branch_id}`,
      contentType: "application/json",
      dataType: "json",
      success: function (data) {
        options = "";
        for (var i = 0; i < data.length; i++) {
          options += `<option value="${data[i].id}">${data[i].name}</option>`;
        }
        empSelection.empty().append(options);
        empSelection.val(0);
        empSelection.selectpicker("refresh");
        $("#employeeSelectSpinner").css("display", "none");
        if (!$('select[id="employee"]').val()) {
          $("#startSurveyBtn").attr("disabled", true);
        }
      },
      error: function (error) {
        console.log(error);
      },
    });
  });

  $("#startSurveyBtn").on("click", function (e) {
    const selectedEmp = $('select[id="employee"]').val();

    // const selectedSurvey = $('select[id="survey"]').val();

    $(this).html("Start Survey");

    $(".queston-choices").each(function () {
      $("input[type=radio]:last", this).attr("checked", true);
    });

    $(`input[type=radio]`).change(function () {
      console.log("changed");
      if ($(this).val() !== "10") {
        $(this).parent().next().css("display", "block");
      } else {
        $(this).parent().next().css("display", "none");
        $(this).parent().next().find("input:first").val("");
      }
    });

    $(".next").click(function (event) {
      event.preventDefault();
      current_fs = $(this).parent();
      next_fs = $(this).parent().next();

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

    let empName = "";
    let empDesignation = "";
    let branchName = "";

    $.ajax({
      type: "GET",
      url: `/api/employees/${selectedEmp}`,
      contentType: "application/json",
      dataType: "json",
      success: function (data) {
        employee = data;
        empName = data.name;
        empDesignation = data.designation;
        branchName = data.branch.name;
        $(".employee-name").html(empName);
        $(".branch-name").html(branchName);
        $(".employee-designation").html(empDesignation);
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
});

function get_query() {
  var url = document.location.href;
  var qs = url.substring(url.indexOf("?") + 1).split("&");
  for (var i = 0, result = {}; i < qs.length; i++) {
    qs[i] = qs[i].split("=");
    result[qs[i][0]] = decodeURIComponent(qs[i][1]);
  }
  return result;
}
