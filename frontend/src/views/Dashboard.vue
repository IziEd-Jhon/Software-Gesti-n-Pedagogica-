<template>


   <div class="flex bg-packed font-lexend dark:bg-gray-900">
    <div
      id="sidebar-scroll"
      class="flex-sidebar lg:flex-auto w-sidebar lg:block hidden bg-white dark:bg-gray-800 border-r-2 dark:border-gray-700 h-screen lg:z-0 z-40 overflow-auto lg:relative fixed"
    >
      <Sidebar />
    </div>
    <div class="flex-auto w-full overflow-auto h-screen" id="body-scroll">
      <Header />
      <Card />
      <Footer />
    </div>
  </div>
</template>

<script>
  // vue Components
  import Sidebar from "@/components/Sidebar";
  import Header from "@/components/Header";
  import Footer from "@/components/Footer";
  import "@/assets/sass/css/windzo.css";
  // npm-js
  import Scrollbar from "smooth-scrollbar";
import Card from "./components/card.vue";

  export default {
    name: "Dashboard",

    components: {
    Header,
    Footer,
    Sidebar,
    Card,
},
    mounted() {

      if (localStorage.getItem('reloaded')) {
        // The page was just reloaded. Clear the value from local storage
        // so that it will reload the next time this page is visited.
        localStorage.removeItem('reloaded');
    } else {
        // Set a flag so that we know not to reload the page twice.
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

      // var acc = document.getElementsByClassName("accordion");
      // var i;
      // for (i = 0; i < acc.length; i++) {
      //   acc[i].addEventListener("click", function () {
      //     this.classList.toggle("active");
      //     var panel = this.nextElementSibling;
      //     if (panel.style.display === "block") {
      //       panel.style.display = "none";
      //       this.classList.remove("bg-gray-100");
      //       this.classList.add("bg-transparent");
      //     } else {
      //       panel.style.display = "block";
      //       this.classList.add("bg-gray-100");
      //       this.classList.remove("bg-transparent");
      //     }
      //   });
      // }
    },
  };
</script>


<style>
.font-semibold  {
  text-align: center;
}

</style>
