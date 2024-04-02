form = document.querySelector("#signupform")
form.addEventListener "submit", (e) ->
    e.preventDefault()
    name = document.getElementById("name").value
    username = document.getElementById("username").value
    password = document.getElementById("password").value
    email = document.getElementById("email").value
    data = {"name": name, "username": username, "email": email, "password": password, "acctype": "student"}
    postJSON(data)

postJSON = (data) ->
  fetch process.env.SIGNUPAPI,
    method: "POST"
    mode: "cors"
    headers:
      "Content-Type": "application/json"
      "Access-Control-Allow-Origin": "*"
      "Access-Control-Allow-Methods": "POST,PATCH,OPTIONS"
    body: JSON.stringify(data)
  .then (response) ->
    if response.ok
      response.json()
    else
      throw {status: response.status, statusText: response.statusText}
  .then (result) ->
    console.log("Success:", result)
    localStorage.setItem("_id", result["data"]["_id"])
    localStorage.setItem("accType" ,result["data"]["accType"])
    window.location.href="../index.html"
    if result.Error
      console.log result.Error
  .catch (error) ->
    # console.error error, error.status
    if error.status==409
      document.getElementById("errorC").style.display="";
      document.getElementById("errorMsg").innerText="Account Already Exists"
    # if error instanceof TypeError and error.message is 'Failed to fetch'
    #   # Handle network errors
    #   console.error('Network error occurred')
    # else
    #   # Handle other types of errors (including 500 Internal Server Errors)
    #   console.error('Internal Server Error occurred')
