function sendMessage() {
  var userInput = document.getElementById("user-input").value;
  var chatDisplay = document.getElementById("chat-display");

  // Display user message
  chatDisplay.innerHTML += "<div>User: " + userInput + "</div>";

  // Here you can add logic to send the user message to the backend or process it further

  // Clear input field
  document.getElementById("user-input").value = "";

  // Scroll chat display to bottom
  chatDisplay.scrollTop = chatDisplay.scrollHeight;
}
