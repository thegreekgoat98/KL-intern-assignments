// function showDate() {
//   <button
//     type="button"
//     onclick="document.getElementById('demo').innerHTML = Date()"
//   >
//     Click me to display Date and Time.
//   </button>;
// }

// Get the clock element
const clock = document.getElementById('clock');

// Function to update the clock
window.onload = function updateClock() {
  const currentTime = new Date();

  // Format the time as HH:MM:SS
  const hours = currentTime.getHours();
  const minutes = currentTime.getMinutes();
  const seconds = currentTime.getSeconds();
  const timeString = hours + ':' + minutes + ':' + seconds;
  console.log(timeString)
  // Update the clock element
  clock.innerHTML = timeString;
  // clock.textContent = timeString;
}

// Call the updateClock function every second
// setInterval(updateClock, 1000);




var users=
[
  {
    user_name:"Chinmoy Ranjan", email:"ranjanchinmoy@gmail.com"
  },
  {
    user_name:"Voona Resmanth", email:"resmanthvoona@gmail.com"
  },
  {
    user_name:"Priyanka", email:"priyanka@gmail.com"
  },
  {
    user_name:"Akhila", email:"akhila@gmail.com"
  },
  {
    user_name:"Dipti", email:"dipti@gmail.com"
  }
]

function showDetails()
{
  userList=[]
  for(var i=0;i<users.length;++i)
  {
    var user = users[i];
    userList.push(user);
    document.write(user.user_name)
  }
}