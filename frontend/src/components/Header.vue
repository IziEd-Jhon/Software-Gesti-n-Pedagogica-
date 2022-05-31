<template>
  <!-- this header -->
  <header class="bg-white dark:bg-gray-800 p-2 border-b-2 dark:border-gray-700">
    <div class="wrap-header flex items-center justify-between flex-wrap">
      <div class="flex flex-no-shrink items-center">
        <button
          class="text-gray-500 lg:hidden ml-3 block"
          @click="sidebarToggle"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            aria-hidden="true"
            role="img"
            width="2em"
            height="2em"
            preserveAspectRatio="xMidYMid meet"
            viewBox="0 0 16 16"
          >
            <path
              fill="none"
              stroke="currentColor"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="1.5"
              d="M2.75 12.25h10.5m-10.5-4h10.5m-10.5-4h10.5"
            />
          </svg>
        </button>
        
      </div>
      <div class="mr-4 flex">
       <button @click="notificationMenuToggle" @blur="notificationMenuToggleBlur" data-dropdown-placement="left" class="mr-1 text-2xl text-gray-500">
          <Icon icon="clarity:notification-line" />
        </button> 
       
     <button
          id="theme-toggle"
          type="button"
          class="text-gray-500 ml-2 dark:text-gray-400  outline-none rounded-lg text-sm p-2.5"
        >
         
         <svg
            id="theme-toggle-light-icon"
            class="hidden w-5 h-5"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
          <path
              d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"
            ></path>
          </svg>
         <img id="theme-toggle-dark-icon" class="hidden w-5 h-5" src="https://img.icons8.com/ios/50/000000/sun--v1.png"/>        
</button>
          <div
          
           >
         
           
            
         <h1 class="p-3 w-full bg-white dark:bg-gray-800 dark:border-gray-700 rounded-md outline-none dark:text-white  ">
          Nombre Apellido <p class="ml-3.5 text-1xl text-green-500"> TEXTO </p>
         </h1>
      

        </div>


   

       
        <button @click="menuToggle" @blur="menuToggleBlur">
          <div
            class="user-avatar flex hover:bg-gray-100 dark:hover:bg-gray-700 p-1 cursor-pointer rounded-md"
          >
            <img
              src="../assets/img/user.jpg"
              class="rounded-full mr-4 w-10 h-10 p-1 ring-1 ring-gray-300 dark:ring-gray-500"
              alt=""
            />
            <span class="text-md mt-4 text-gray-300"
              ><Icon icon="bi:caret-down-fill"
            /></span>
          </div>
        </button>

        <transition name="fade">
          <div
            id="dropdownSmall"
            v-show="menu" 
            class="block absolute right-10 mt-12 z-10 w-44 border dark:border-gray-700 bg-white dark:bg-gray-800 rounded divide-y dark:divide-gray-700 divide-gray-100 shadow"
          >
            <div class="py-3 px-4 text-sm text-gray-900 dark:text-gray-200 hover:bg-green-600 hover:text-white"   >
              <div>Sesion Iniciada como</div>
              <div class="font-medium truncate">Usuario</div>
            </div>
            <ul
              class="py-1 text-sm dark:bg-gray-800 text-gray-700 dark:bg-gray-800 dark:text-gray-200"
              aria-labelledby="dropdownSmallButton"
            >
              <li>
                <a
                  href="#"
                  class="block py-2 px-4 hover:bg-green-600 hover:text-white" 
                  >Perfil</a
                >
              </li>
              <li>
                <a
                  href="#"
                  class="block py-2 px-4 hover:bg-green-600 hover:text-white" 
                  >Opciones</a
                >
              </li>
              <li>
              
              </li>
            </ul>
            <div class="py-1" >
              <a
                href="#"
                class="block py-2 px-4 text-sm text-gray-700 dark:text-gray-200 hover:bg-green-600  hover:text-white"
                >Cerrar Sesión</a
              >
            </div>
          </div>
        </transition>

        <transition name="fade">
          <div
            id="dropdownSmall"
            v-show="notificationMenu"  
            class="block absolute left-5 mt-12 z-10 w-44 border dark:border-gray-700 bg-white dark:bg-gray-800 rounded divide-y dark:divide-gray-700 divide-gray-100 shadow"
          >
            <div class="py-4 px-4 text-sm text-gray-900 dark:text-gray-200 hover:bg-green-600 hover:text-white "   >
              <div class="font-medium">Notificacion</div>
              <p class="truncate">Texto Notificación</p>
            </div>
      <div class="py-4 px-4 text-sm text-gray-900 dark:text-gray-200 hover:bg-green-600 hover:text-white "   >
              <div class="font-medium">Notificacion</div>
              <p class="truncate">Texto Notificación</p>
            </div>
            
           
          </div>
        </transition>
      </div>
    </div>
  </header>
</template>

<script>
  const html = document.querySelector("html");
  import { Icon } from "@iconify/vue";
  export default {
    data() {
      return {
        menu: false,
        notificationMenu:false,
      };
    },
    components: {
      Icon,
    },
    methods: {
      menuToggle: function () {
        this.menu = !this.menu;
      },
      menuToggleBlur: function () {
        this.menu = false;
      },
      notificationMenuToggle: function () {
        this.notificationMenu = !this.menu;
      },
      notificationMenuToggleBlur: function () {
        this.notificationMenu = false;
      },
      sidebarToggle: function () {
        document.querySelector(".flex-sidebar").classList.remove("hidden");
      },
    },
    mounted() {
      var themeToggleDarkIcon = document.getElementById(
        "theme-toggle-dark-icon"
      );
      var themeToggleLightIcon = document.getElementById(
        "theme-toggle-light-icon"
      );

      // Change the icons inside the button based on previous settings
      if (
        localStorage.getItem("color-theme") === "dark" ||
        !("color-theme" in localStorage)
      ) {
        html.classList.add("dark")
        document.getElementById("logo-image-black").src="https://i.ibb.co/j3zrBq2/logo-blanco.png";

        themeToggleLightIcon.classList.remove("hidden");
      } else {
        document.getElementById("logo-image-black").src="https://i.ibb.co/VLJpWS2/logo-oscuro.png";
        document.documentElement.classList.remove("dark");
        themeToggleDarkIcon.classList.remove("hidden");
      }

     

      var themeToggleBtn = document.getElementById("theme-toggle");

      themeToggleBtn.addEventListener("click", function () {
        // toggle icons inside button
        themeToggleDarkIcon.classList.toggle("hidden");
        themeToggleLightIcon.classList.toggle("hidden");

        // if set via local storage previously
        if (localStorage.getItem("color-theme")) {
          if (localStorage.getItem("color-theme") === "light") {
            html.classList.add("dark");
            document.getElementById("logo-image-black").src="https://i.ibb.co/j3zrBq2/logo-blanco.png";

            localStorage.setItem("color-theme", "dark");
          } else {
            html.classList.remove("dark");
            document.getElementById("logo-image-black").src="https://i.ibb.co/VLJpWS2/logo-oscuro.png";
            localStorage.setItem("color-theme", "light");
          }

          // if NOT set via local storage previously
        } else {
          if (document.documentElement.classList.contains("dark")) {
            html.classList.remove("dark");
            document.getElementById("logo-image-black").src="https://i.ibb.co/VLJpWS2/logo-oscuro.png";

            localStorage.setItem("color-theme", "light");
          } else {

            html.classList.add("dark");
            document.getElementById("logo-image-black").src="https://i.ibb.co/j3zrBq2/logo-blanco.png";
            localStorage.setItem("color-theme", "dark");
          }
        }
      });
    },
  };
</script>
