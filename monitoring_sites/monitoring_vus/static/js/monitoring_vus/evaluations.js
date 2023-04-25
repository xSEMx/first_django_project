const modal = document.getElementById("modal");
const telegramContent = document.getElementById("telegram-content");
const emailContent = document.getElementById("email-content");
const telegramButton = document.getElementById("telegram-button");
const emailButton = document.getElementById("email-button");
const closeBtn = document.getElementsByClassName("close")[0];

telegramButton.onclick = function() {
  modal.style.display = "block";
  telegramContent.style.display = "block";
}

emailButton.onclick = function() {
  modal.style.display = "block";
  emailContent.style.display = "block";
}

closeBtn.onclick = function() {
  modal.style.display = "none";
  telegramContent.style.display = "none";
  emailContent.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
    telegramContent.style.display = "none";
    emailContent.style.display = "none";
  }
}

window.addEventListener('load', function() {
  var formError = document.getElementById('comment-section').getAttribute('data-errors');
  
        if (formError === 'true') {
          document.getElementById("comment").querySelector('#read').style.display = 'none';
          document.getElementById("comment").querySelector('#edit').style.display = 'block';
      } 
});

function makeEditable(containerId) {
    var readDiv = document.getElementById(containerId).querySelector('#read');
    var editDiv = document.getElementById(containerId).querySelector('#edit');

    if (readDiv.style.display === 'none') {
        readDiv.style.display = 'block';
        editDiv.style.display = 'none';
    } else {
        readDiv.style.display = 'none';
        editDiv.style.display = 'block';
    }
}