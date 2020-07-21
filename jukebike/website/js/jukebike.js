function connect() {

    var apiBaseUrl = window.location.protocol + '//' + window.location.host.replace('www.', 'api.')

    fetch(apiBaseUrl + '/search')
      .then(function(response) {
          if (response.status !== 200) {
            console.log('Looks like there was a problem. Status Code: ' + response.status);
            result = 'Could not connect';
           }
          // Examine the text in the response
          response.json().then(function(data) {
                result = data[0].name;
                const app = document.getElementById('statustext');
                app.textContent = result;

              var table = document.createElement("TABLE");
              table.style.textAlign = "left";
              //table.setAttribute("id", "searchResultTable");
              app.appendChild(table);

              for (i = 0; i < data.length; i++) {
                  var row = document.createElement("TR");
                  table.appendChild(row)

                  var cell_name = document.createElement("TD");
                  var cell_artist = document.createElement("TD");
                  var cell_length = document.createElement("TD");
                  cell_name.textContent = data[i].name;
                  cell_artist.textContent = data[i].artist;
                  cell_length.textContent = data[i].length;
                  row.appendChild(cell_name);
                  row.appendChild(cell_artist);
                  row.appendChild(cell_length);
                }
          })
      })
      .catch(function(err) {
        console.log('Fetch Error :-S', err);
        result = err;
      });
}
