$(document).ready(function () {
  $("#createBranchForm").submit(function () {
    $("#saveBranchSpinner").css("display", "block");
    $("#saveBranchSpinner").addClass("d-inline-block");
    $("#saveBranchBtn").prop("disabled", true);
    $("#saveBranchBtn span").text("Saving");
  });

  $(".delete-branch-btn").on("click", function () {
    $("#deleteBranchForm").find("input:first").val($(this).data("branch-id"));
  });

  $("#deleteBranchForm").on("submit", function (e) {
    e.preventDefault();

    $("#deleteBranchSpinner").css("display", "block");
    $("#deleteBranchSpinner").addClass("d-inline-block");
    $("#deleteBranchBtn").prop("disabled", true);
    $("#deleteBranchBtn span").text("Deleting");

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
