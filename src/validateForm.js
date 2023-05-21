function validateForm() {
  var commandInput = document.getElementById("command");
  var commandValue = commandInput.value.trim();

  if (commandValue === "") {
    commandInput.classList.add("border-red-700");
    return false;
  }

  return true;
}
