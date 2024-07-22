$(document).ready(function() {
    // Tab functionality
    $('#myTab a').on('click', function(e) {
        e.preventDefault();
        $(this).tab('show');
    });

    // DataTable initialization
    $('#my-orders-table').DataTable({
        responsive: true,
        "pageLength": 10,
        "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]]
    });

    // My account nav click functionality
    $('.tg-tabs-content-wrapp .my-account-dashboard .card').click(function() {
        var ariaClick = $(this).attr('area-toggle');
        $('.tg-account .account-banner .nav-area a#' + ariaClick).tab('show');
    });

    // Form submission prevention (for demonstration)
    $('form.tg-form').submit(function(e) {
        e.preventDefault();
        alert('Form submission prevented for demonstration purposes.');
    });

    // View Order button click handler
    $(document).on('click', 'a.view-order', function(e) {
        e.preventDefault();
        var orderId = $(this).closest('tr').find('td:first').text();
        alert('Viewing Order: ' + orderId);
    });

    // Highlight active card in dashboard
    function highlightActiveCard() {
        var activeTabId = $('.nav-tabs .active').attr('id');
        $('.my-account-dashboard .card').removeClass('active');
        $('.my-account-dashboard .card[area-toggle="' + activeTabId + '"]').addClass('active');
    }

    // Call highlightActiveCard on page load and tab change
    highlightActiveCard();
    $('a[data-toggle="tab"]').on('shown.bs.tab', highlightActiveCard);
    
  document.getElementById("logout-btn").addEventListener("click", function() {
    // Add your logout logic here, such as making an AJAX request to a logout endpoint
    console.log("Logout button clicked!");

});
});