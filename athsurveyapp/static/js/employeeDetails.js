$(document).ready(function(){

    $('#employeesTable').DataTable();

    $('.response-date').each(function(){
        const responseDate = new Date($(this).text()).toLocaleDateString(undefined, {
            weekday: "long",
            year: "numeric",
            month: "long",
            day: "numeric",
          });

          $(this).html(responseDate);
    });


      

});