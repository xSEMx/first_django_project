window.addEventListener('load', function() {
	var formError = document.getElementById('comment-section').getAttribute('data-errors');
  	var comments = document.getElementById('comment-section').getAttribute('data-comments');
        var comId = document.getElementById('comment-section').getAttribute('data-com-id');

        if (formError === 'true') {
      		document.getElementById("content").style.display = 'block';
      		document.getElementById(comId).querySelector('#read').style.display = 'none';
      		document.getElementById(comId).querySelector('#edit').style.display = 'block';
    	} 
        else if (comments === 'true') {
      		document.getElementById("content").style.display = 'block';
    	}
	

	var div = document.getElementById("content");
    	var btn = document.getElementById("toggleBtn");

    	if (div.style.display === "none") {
        	btn.innerHTML = "Показать";
    	} else {
        	btn.innerHTML = "Скрыть";
    	}
});

function toggleVisibility() {
	var div = document.getElementById("content");
    	var btn = document.getElementById("toggleBtn");

    	if (div.style.display === "none") {
     		div.style.display = "block";
        	btn.innerHTML = "Скрыть";
    	} else {
        	div.style.display = "none";
        	btn.innerHTML = "Показать";
    	}
}

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