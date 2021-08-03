$(document).ready(function() {

    $('select[id="survey"]').change(function() {
    $("form").children("fieldset").each(function(index){
      if(index > 0) {
        $(this).remove();
      }
    });

      $.ajax({
        type: "GET",
        url: `/api/surveys/${$(this).val()}`,
        contentType: "application/json",
        success: function(data) {
            let fieldsetCategory = "";
            const surveyName = data.name
            $(".survey-name").html(data.name)
            
            for (let i = 0; i < data.question_types.length; i++) {

                
                let questions = "";
                
                data.question_types[i].questions.forEach(question => {

                    let choices = "";

                    for (let k = 0; k < question.choice.value; k++) {

                        choices += `
                        <input style="display: none;" class="form-check-input" type="radio" name="${question.id}" id="${question.description + k}" value="${k + 1}">
                        <label class="form-check-label" for="${question.description + k}">${k + 1}</label>
                        `;
                        
                    }
                    
                    questions += `
                    <tr>
                        <td class="w-50">
                            <label class="font-weight-bold">${question.description}</label>
                        </td>
                        <td>
                            <div class="form-check form-check-inline d-flex justify-content-between">${choices}</div>
                            <div class="form-group py-3 mt-3" style="display: none;">
                                <input type="text" class="form-control" placeholder="Please provide reason why less than 10">
                            </div>
                        </td>

                     </tr>

                    `;

                });

                fieldsetCategory += `
                <fieldset style="display: none;">
                <div class="row">
                    <div class="col-6">
                        <p><span class="text-muted">Date:</span> <span class="font-weight-bold">DATE TODAY</span></p>
                    </div>
                    <div class="col-6">
                        <p><span class="text-muted">Branch:</span> <span class="font-weight-bold branch-name" ></span></p>
                    </div>
                    <div class="col-6">
                        <p><span class="text-muted">Name:</span> <span class="font-weight-bold employee-name"></span></p>
                    </div>
                    <div class="col-6">
                        <p><span class="text-muted">Designation:</span> <span class="font-weight-bold employee-designation"></span></p>
                    </div>
                    <div class="col-6">
                        <p><span class="text-muted">Surveyor:</span> <span class="font-weight-bold survey-name">${surveyName}</span></p>
                    </div>
                    <div class="col-6">
                        <p><span class="text-muted">Surveyor:</span> <span class="font-weight-bold">USER NAME</span></p>
                    </div>
                </div>

                <div class="row mt-5">
                    <div class="col-12">
                        <h1 class="font-weight-bold">${data.question_types[i].description}</h1>
    
                    </div>
                    <table class="table table-hover mt-5 px-5" id="tableSurvey">
                        <tbody>
                        ${questions}
                        </tbody>
                    </table>
                </div>

                <button class="btn btn-secondary previous mt-5">Back</button>
                ${data.question_types.length == i + 1 ? '<button type="submit" class="btn btn-info mt-5">Submit</button>' : '<button class="btn btn-info next mt-5">Next</button>' }
            </fieldset>`;
            

            }
            $("form").append(fieldsetCategory);
        },
        error: function(error) {
            console.log(error);
        }
    });
    })

    $('select[id="branch"]').on('change', function(e){
        const branch_id = e.target.value;

        const empSelection = $('select[id="employee"]');

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
            },
            error: function (error) {
              console.log(error);
            },
          });
    });


    $("#startSurveyBtn").on("click", function(e){
        const selectedEmp = $('select[id="employee"]').val();
        // const selectedSurvey = $('select[id="survey"]').val();
        console.log("clicked");
        $(this).html("Start Survey")

        $('input:radio').each(function(){
          console.log($(this));

        });

        // $(`input[name=${question.id}]`).change(function(){
        //   console.log("changed");
        //     if($(this).val() !== '10') {
        //         $(this).parent().next().css("display", "block");
        //     } else {
        //         $(this).parent().next().css("display", "none");
        //     }
        // });

      
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

        let empName = ""
        let empDesignation = ""
        let branchName = ""

        $.ajax({
            type: "GET",
            url: `/api/employees/${selectedEmp}`,
            contentType: "application/json",
            dataType: "json",
            success: function (data) {
                empName = data.name
                empDesignation = data.designation
                branchName = data.branch.name
                $(".employee-name").html(empName);
                $(".branch-name").html(branchName);
                $(".employee-designation").html(empDesignation);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

    
});