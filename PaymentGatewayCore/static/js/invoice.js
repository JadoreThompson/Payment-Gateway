document.addEventListener('DOMContentLoaded', function(){
    const baseUrl = "http://127.0.0.1:8000/dashboard/invoice";

    const allInvoicesTitle = document.getElementById('all-invoices-button');
    const draftInvoicesTitle = document.getElementById('draft-invoices-button');
    const paidInvoicesTitle = document.getElementById('paid-invoices-button');
    const unpaidInvoicesTitle = document.getElementById('unpaid-invoices-button');

    allInvoicesTitle.addEventListener('click', function() {
        console.log('All Invoices clicked');
        window.location.href = baseUrl;
    });

    draftInvoicesTitle.addEventListener('click', function() {
        console.log('Draft Invoices clicked');
        window.location.href = baseUrl + "?status=draft";
    });

    paidInvoicesTitle.addEventListener('click', function() {
        console.log('Paid Invoices clicked');
        window.location.href = baseUrl + "?status=paid";
    });

    unpaidInvoicesTitle.addEventListener('click', function() {
        console.log('Unpaid Invoices clicked');
        window.location.href = baseUrl + "?status=unpaid";
    });
});