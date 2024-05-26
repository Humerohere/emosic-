// document.addEventListener("DOMContentLoaded", function() {
   
//     document.querySelector(".connection").addEventListener("click", function(event) {
//         event.preventDefault(); // Prevent default action of the button

//         navigator.mediaDevices.getUserMedia({ video: true })
//             .then(function(stream) {
//                 // Success callback - stream contains the camera feed
//                 console.log("Camera feed opened successfully");

//                 // Display camera feed
//                 var videoElement = document.createElement('video');
//                 videoElement.srcObject = stream;
//                 videoElement.autoplay = true;
//                 videoElement.classList.add('camera-feed');

//                 // Append video element to the document body or a container
//                 document.body.appendChild(videoElement);
//             })
//             .catch(function(error) {
//                 // Error callback - handle errors here
//                 console.error("Error opening camera feed:", error);
//             });
//     });
// });

document.addEventListener("DOMContentLoaded", function() {
    document.querySelector(".connection").addEventListener("click", function(event) {
        event.preventDefault();

       
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function(stream) {
               
                console.log("Camera feed opened successfully");

              
                var videoElement = document.createElement('video');
                videoElement.srcObject = stream;
                videoElement.autoplay = true;
                videoElement.classList.add('camera-feed');
                document.body.appendChild(videoElement);

                
                fetch('/detect-emotion', {
                    method: 'POST',
                    body: JSON.stringify({}),
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                .then(function(response) {
                    return response.json();
                })
                .then(function(data) {
                   
                    fetch('/recommend-songs', {
                        method: 'POST',
                        body: JSON.stringify({ emotion: data.emotion }),
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    })
                    .then(function(response) {
                        return response.json();
                    })
                    .then(function(songs) {
                       
                        displaySongRecommendations(songs);
                    })
                    .catch(function(error) {
                        console.error("Error fetching song recommendations:", error);
                    });
                })
                .catch(function(error) {
                    console.error("Error fetching face emotion:", error);
                });
            })
            .catch(function(error) {
                console.error("Error opening camera feed:", error);
            });
    });
});

function displaySongRecommendations(songs) {
    // Display songs on the webpage
    var playlistContent = document.querySelector('.playlist-content ul');
    playlistContent.innerHTML = ''; 

    songs.forEach(function(song) {
        var listItem = document.createElement('li');
        listItem.className = 'playlist-number';
        listItem.innerHTML = `
            <div class="song-info">
                <h4>${song.title}</h4>
                <p><strong>Album</strong>: ${song.album} &nbsp;|&nbsp; <strong>Type</strong>: ${song.type} &nbsp;|&nbsp; <strong>Singer</strong>: ${song.singer}</p>
            </div>
            <div class="clearfix"></div>
        `;
        playlistContent.appendChild(listItem);
    });
}

