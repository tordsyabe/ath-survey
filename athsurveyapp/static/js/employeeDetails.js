$(document).ready(function () {
  $("#employeesTable").DataTable();

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

  $(".view-detailed-response").on("click", function (e) {
    e.preventDefault();
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
          <div class="row py-2">
            <div class="col-6">${data.question_responses[i].question}</div>
            <div class="col-1">${data.question_responses[i].answer}</div>
            <div class="col-3">${data.question_responses[i].feedback}</div>
        </div>
         `;
        }
        $("#reponseDetails").append(responseDetail);
      },
    });
  });
  $(".delete-reponse").on("click", function () {
    const responseId = $(this).data("delete-id");

    $("#deleteResponseForm").find("input:first").val(responseId);
  });

  $("#deleteResponseForm").submit(function (e) {
    const reponseToDelete = $(this).find("input:first").val();
    e.preventDefault();
    $.ajax({
      type: "DELETE",
      url: "/api/employees/responses/" + reponseToDelete,
      success: function (data) {},
      error: function (error) {
        console.log(error);
      },
    });
  });
});
