function searchICD() {
    var searchTerm = document.getElementById('searchInput').value;
  
    // Create a new XMLHttpRequest object
    var xhr = new XMLHttpRequest();
    
    // Define the request URL
    var url = 'https://your-api-endpoint.com/search?term=' + searchTerm;
    
    // Set up the request
    xhr.open('GET', url, true);
  
    // Set the response type to XML
    xhr.responseType = 'document';
  
    // Define the onload function
    xhr.onload = function() {
      if (xhr.status === 200) {
        var responseXML = xhr.responseXML;
        var searchResults = responseXML.getElementsByTagName('result');
  
        var searchResultsContainer = document.getElementById('searchResults');
        searchResultsContainer.innerHTML = ''; // Clear previous results
  
        // Iterate over the search results
        for (var i = 0; i < searchResults.length; i++) {
          var code = searchResults[i].getElementsByTagName('code')[0].textContent;
          var description = searchResults[i].getElementsByTagName('description')[0].textContent;
  
          var resultDiv = document.createElement('div');
          var codeHeading = document.createElement('h3');
          codeHeading.textContent = code;
          var descriptionPara = document.createElement('p');
          descriptionPara.textContent = description;
  
          resultDiv.appendChild(codeHeading);
          resultDiv.appendChild(descriptionPara);
          searchResultsContainer.appendChild(resultDiv);
        }
      }
    };
  
    // Send the request
    xhr.send();
  }
  