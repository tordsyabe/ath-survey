$(document).ready(function() {
    $('select[id="branch"]').on('change', function(e){
        const branch_id = e.target.value;

        const empSelection = $('select[id="employee"]');
        console.log(branch_id);

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
});