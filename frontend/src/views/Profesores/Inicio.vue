<template>


   <div class="flex bg-packed font-lexend dark:bg-gray-900">
    <div
      id="sidebar-scroll"
      class="flex-sidebar dark:bg-white lg:flex-auto w-sidebar lg:block hidden bg-white dark:bg-gray-800 border-r-2 dark:border-gray-700 h-screen lg:z-0 z-40 overflow-auto lg:relative fixed"
    >
      <Sidebar />
    </div>
    <div class="flex-auto w-full overflow-auto h-screen" id="body-scroll">
      <Header />
      <InicioContenido />
      <Footer />
    </div>
  </div>
</template>

<script>
  // vue Components
  import Sidebar from "@/components/ProfesorComponentes/SidebarProfesor";
  import Header from "@/components/Header";
  import Footer from "@/components/Footer";
  import "@/assets/sass/css/windzo.css";
  // npm-js
import Scrollbar from "smooth-scrollbar";

  export default {
    name: "InicioProfesor",

    components: {
    Header,
    Footer,
    Sidebar,
    
},
    mounted() {

      if (localStorage.getItem('reloaded')) {
      
        localStorage.removeItem('reloaded');
    } else {
        localStorage.setItem('reloaded', '1');
        location.reload();
    }
      Scrollbar.init(document.querySelector("#body-scroll"));

      setTimeout(() => {
        var alert_dis = document.querySelectorAll(".alert-dismiss");
        alert_dis.forEach((x) =>
          x.addEventListener("click", function () {
            x.parentElement.classList.add("hidden");
          })
        );
      }, 100);

       Scrollbar.init(document.querySelector("#body-scroll"));

      setTimeout(() => {
        var alert_dis = document.querySelectorAll(".alert-dismiss");
        alert_dis.forEach((x) =>
          x.addEventListener("click", function () {
            x.parentElement.classList.add("hidden");
          })
        );
      }, 100);

       var acc = document.getElementsByClassName("accordion");
       var i;
       for (i = 0; i < acc.length; i++) {
         acc[i].addEventListener("click", function () {
           this.classList.toggle("active");
           var panel = this.nextElementSibling;
           if (panel.style.display === "block") {
             panel.style.display = "none";
             this.classList.remove("bg-gray-100");
             this.classList.add("bg-transparent");
           } else {
             panel.style.display = "block";
             this.classList.add("bg-gray-100");
             this.classList.remove("bg-transparent");
           }
         });
       }
    },
  };
</script>


<style>
.font-semibold  {
  text-align: center;
}

#sidebar-scroll::-webkit-scrollbar-track
{
	-webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
	border-radius: 10px;
	background-color: #F5F5F5;
}

#sidebar-scroll::-webkit-scrollbar
{
	width: 12px;
	background-color: #F5F5F5;
}

#sidebar-scroll::-webkit-scrollbar-thumb
{
	border-radius: 10px;
	-webkit-box-shadow: inset 0 0 6px rgba(0,0,0,.3);
	background-color: #555;
}


</style>
