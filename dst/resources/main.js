function contactEmail() {
    var name = document.getElementById("name").value;
    var phone = document.getElementById("phone").value;
    var subject = document.getElementById("subject").value;
    var message = document.getElementById("message").value;
    window.location.href = 
`mailto:funderburgfinishes@yahoo.com?subject=${subject}&body=${message}%0D%0A%0D%0A
Contact Name: ${name}%0D%0A
Contact Phone Number: ${phone}`;
}