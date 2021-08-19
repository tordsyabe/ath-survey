$(document).ready(function () {
  $("#deleteBranchBtn").on("click", function () {
    $("#deleteBranchForm").find("input:first").val($(this).data("branch-id"));
  });

  $("#deleteBranchForm").on("submit", function (e) {
    e.preventDefault();
    const branchId = $(this).find("input:first").val();

    $.ajax({
      type: "DELETE",
      url: "/api/branches/" + branchId,
      success: function (data) {
        location.href = "/branches/";
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
});
