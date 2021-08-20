$(document).ready(function () {
  $("#employeesTable").DataTable();

  $("#saveEmployeeDetailForm").submit(function () {
    $("#saveEmployeeDetailSpinner").css("display", "block");
    $("#saveEmployeeDetailSpinner").addClass("d-inline-block");
    $("#saveEmployeeDetailBtn").prop("disabled", true);
    $("#saveEmployeeDetailBtn span").text("Saving");
  });

  $("#createEmployeForm").submit(function () {
    $("#saveEmployeeSpinner").css("display", "block");
    $("#saveEmployeeSpinner").addClass("d-inline-block");
    $("#saveEmployeeBtn").prop("disabled", true);
    $("#saveEmployeeBtn span").text("Saving");
  });
  // DELETE EMPLOYEE
  $("#deleteEmployeeForm").submit(function (e) {
    e.preventDefault();
    $("#deleteEmployeeSpinner").css("display", "block");
    $("#deleteEmployeeSpinner").addClass("d-inline-block");
    $("#deleteEmployeeeBtn").prop("disabled", true);
    $("#deleteEmployeeeBtn span").text("Deleting");
    const employeeToDelete = $(this).find("input:first").val();
    e.preventDefault();
    $.ajax({
      type: "DELETE",
      url: "/api/employees/" + employeeToDelete,
      success: function (data) {
        location.href = "/employees";
      },
      error: function (error) {
        console.log(error);
      },
    });
  });

  $(".response-date").each(function () {
    const responseDate = new Date($(this).text()).toLocaleDateString(
      undefined,
      {
        weekday: "long",
        year: "numeric",
        month: "long",
        day: "numeric",
      }
    );

    $(this).html(responseDate);
  });
  // GET RESPONSE DETAIL
  $(".view-detailed-response").on("click", function (e) {
    e.preventDefault();

    $("#viewDetailsSpinner").css("display", "block");
    $("#viewDetailsSpinner").addClass("d-inline-block");
    $(this).prop("disabled", true);
    $(this).find("span").text("Getting Details");

    const responseId = $(this).data("details-id");

    $.ajax({
      type: "GET",
      url: `/api/employees/responses/${responseId}`,
      contentType: "application/json",
      success: function (data) {
        $("#reponseDetails").children().remove();
        responseDetail = "";
        for (var i = 0; i < data.question_responses.length; i++) {
          responseDetail += `
              <tr>
                <td>${data.question_responses[i].question}</td>
                <td>${data.question_responses[i].answer}</td>
                <td>${data.question_responses[i].feedback}</td>
              </tr>
         `;
        }
        $("#reponseDetails").append(responseDetail);
        $("#reponseDetails").append(`
          <div class="row mt-5">
            <div class="col-12">
              <p class="font-weight-bold">Conducted By: ${data.user.name}</p>
            </div>
          </div>
        `);

        $("#viewDetailsSpinner").css("display", "none");
        $("#viewDetailsSpinner").removeClass("d-inline-block");
        $(".view-detailed-response").prop("disabled", false);
        $(".view-detailed-response").find("span").text("View Details");

        $("#responseDetailModal").modal("toggle");
      },
      error: function (e) {
        console.log(e);
      },
    });
  });
  $(".delete-reponse").on("click", function () {
    const responseId = $(this).data("delete-id");

    $("#deleteResponseForm").find("input:first").val(responseId);
  });
  // DELETE RESPOSE
  $("#deleteResponseForm").submit(function (e) {
    const reponseToDelete = $(this).find("input:first").val();
    e.preventDefault();

    $("#deleteResponseSpinner").css("display", "block");
    $("#deleteResponseSpinner").addClass("d-inline-block");
    $("#deleteResponseBtn").prop("disabled", true);
    $("#deleteResponseBtn span").text("Deleting");

    $.ajax({
      type: "DELETE",
      url: "/api/employees/responses/" + reponseToDelete,
      success: function (data) {
        location.href =
          "/employees/" +
          $("#deleteResponseForm").find("input[name='employeeId']").val();
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
});
