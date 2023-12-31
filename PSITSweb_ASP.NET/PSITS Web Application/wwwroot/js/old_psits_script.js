﻿
function home() {
    location.href = "/PSITS";
}



function createNewEvent() {
    location.href = "/PSITS@NewEvent"
}

function studentsInfo() {
    location.href = "/PSITS@Students"
}

// PSITS@Event
//NOTICE!!!
function requiredPayment(checkbox) {
    document.getElementById('item_field').style.display = checkbox.checked ? 'block' : 'none';
    document.getElementById('amount_field').style.display = checkbox.checked ? 'block' : 'none';
}

function register() {
    location.href = "/PSITS@Register"
}

function onChange() {
    const password = document.querySelector('input[name=password]');
    const confirm = document.querySelector('input[name=confirm]');
    if (confirm.value === password.value) {
        confirm.setCustomValidity('');
    } else {
        confirm.setCustomValidity('Passwords do not match');
    }
}

if (document.getElementById("Date") != null) {
    document.getElementById("Date").valueAsDate = new Date()
}


function search_student() {
    var input = document.getElementById("search_student")
    if (input != null)
        location.href = "/PSITS@Students/" + input.value + "";
}

function edit_studentInfo(uid) {
    if (document.getElementById(uid + "idno").disabled == true) {
        document.getElementById(uid + "rfid").disabled = false;
        document.getElementById(uid + "lastname").disabled = false;
        document.getElementById(uid + "firstname").disabled = false;
        document.getElementById(uid + "course").disabled = false;
        document.getElementById(uid + "year").disabled = false;
        document.getElementById(uid + "email").disabled = false;
        document.getElementById(uid + "edit").style.display = 'none';
        document.getElementById(uid + "button").hidden = false;
    }

}

function update_order(uid) {
    if (document.getElementById(uid + "uid").disabled == true) {
        if (document.getElementById(uid + "status").value === "ORDERED" || document.getElementById(uid + "status").value === "PAID") {
            document.getElementById(uid + "status").disabled = false;
            document.getElementById(uid + "button").hidden = false;
            document.getElementById(uid + "edit").hidden = true;
        }
    }
}

function on_paid_order(status, uid) {
    if (status === "PAID") {
        document.getElementById(uid + "reference").disabled = false;
        document.getElementById(uid + "reference").required = true;
    } else {
        document.getElementById(uid + "reference").disabled = true;
        document.getElementById(uid + "reference").required = false;
    }
}

// deprecated
function edit_eventInfo(uid) {
    if (document.getElementById(uid + "uid").disabled == true) {
        document.getElementById(uid + "title").disabled = false;
        document.getElementById(uid + "date_held").disabled = false;
        document.getElementById(uid + "info").disabled = false;
        document.getElementById(uid + "required_payment").disabled = false;
        document.getElementById(uid + "item").disabled = false;
        document.getElementById(uid + "amount").disabled = false;
        document.getElementById(uid + "button").hidden = false;
        document.getElementById(uid + "open_for_payment").disabled = false;
        document.getElementById(uid + "edit").style.display = 'none';
    }
}

function EDITEventList(uid) {
    if (document.getElementById(uid + "uid").disabled == true) {
        document.getElementById(uid + "title").disabled = false;
        document.getElementById(uid + "date_published").disabled = false;
        document.getElementById(uid + "information").disabled = false;
        document.getElementById(uid + "image_file").disabled = false;
        document.getElementById(uid + "save").hidden = false;
        document.getElementById(uid + "edit").style.display = 'none';
    }
}

function open_payment_notification(uid) {
    if (document.getElementById(uid + 'open_for_payment').value === 'YES')
        if (confirm("Do you confirm that selecting 'YES' option for 'Open for Payment' will notify all accounts that are in reservation") === false) {
            document.getElementById(uid + 'open_for_payment').value = 'NO'
        }
}

function order_sum_total(qty, amount) {
    document.getElementById('total_display').innerHTML = "Total: " + (parseInt(qty) * parseInt(amount)).toFixed(2);
    document.getElementById('total_amount').innerHTML = (parseInt(qty) * parseInt(amount)).toFixed(2);
}

function required_payment_check(selector, uid) {
    if (selector != null) {
        if (selector.value == "NO") {
            document.getElementById(uid + "item").value = '';
            document.getElementById(uid + "amount").value = 0.0;
        }
    }
}
function deleteStudent(uid) {
    if (confirm("Are you sure you want to delete student id[" + uid + "]?") === true) {
        location.href = "/PSITS@StudentRemove/" + uid;
    }
}

function deleteEvent(uid) {
    if (confirm("Are you sure you want to delete event id[" + uid + "]?") === true) {
        location.href = "/PSITS@EventRemove/" + uid;
    }
}

function deleteAnnouncement(uid) {
    if (confirm("Are you sure you want to delete this announcement?") === true) {
        location.href = "/announcement_removal/" + uid;
    }
}

function closeEventModal() {
    location.href = '/PSITS'
}

function showEvents() {
    location.href = "/PSITS@Events"
}

function showOrders() {
    location.href = "/PSITS@Orders"
}

function merchandise() {
    location.href = "/PSITS@Merchandise"
}

function loadCSVTemplate(option, search) {
    if (search === '')
        search = 'all';
    location.href = "/PSITS@CSVdata/" + option + "/" + search;
}

function removeMerchandise(uid) {
    if (confirm("Are you sure you want to delete this merchandise?") === true) {
        location.href = "/PSITS@RemoveMerch/" + uid;
    }
}

function editOfficerInfo(uid) {
    if (document.getElementById(uid + 'idno').disabled === true) {
        document.getElementById(uid + 'position').disabled = false;
        document.getElementById(uid + 'birthday').disabled = false;
        document.getElementById(uid + 'edit').hidden = true;
        document.getElementById(uid + 'button').hidden = false;
    }
}

function editMerchInfo(uid) {
    if (document.getElementById(uid + 'uid').disabled === true) {
        document.getElementById(uid + 'title').disabled = false;
        document.getElementById(uid + 'info').disabled = false;
        document.getElementById(uid + 'price').disabled = false;
        document.getElementById(uid + 'discount').disabled = false;
        document.getElementById(uid + 'stock').disabled = false;
        document.getElementById(uid + 'edit').hidden = true;
        document.getElementById(uid + 'button').hidden = false;
    }
}

function editOrderStatus(uid) {
    if (document.getElementById(uid + 'idnum').hidden === true) {
        document.getElementById(uid + 'status').disabled = false;
        document.getElementById(uid + 'edit').hidden = true;
        document.getElementById(uid + 'button').hidden = false;
    }
}

function deleteOrder(uid) {
    if (confirm("Are you sure you want to delete this order? id=> " + uid) === true) {
        location.href = "/PSITS@RemoveOrder/" + uid;
    }
}

function disable(doc) {
    doc.hidden = true;
}

function deleteOfficer(uid) {
    if (confirm("Are you sure you want to delete this officer? id=> " + uid) === true) {
        location.href = "/PSITS@RemoveOfficer/" + uid;
    }
}

function checkStockOverOrder() {
    let stock = 0;
    let order = 0;

    stock = parseInt(document.getElementById("merch_stock").value);
    order = parseInt(document.getElementById("quantity").value);

    if (order > stock) {
        console.log(stock);
        console.log(order);
        document.getElementById("submitBTN").disabled = true;
        document.getElementById("submitBTN").style.background = 'grey';
        alert("You order is over the stock available. Please reduce your number of order");

    }
    else {
        document.getElementById("submitBTN").disabled = false;
        document.getElementById("submitBTN").style.background = '#004064';
    }
}
