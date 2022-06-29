<template>
  <!-- sidebar -->
  <nav class="sidebar bg-white dark:bg-gray-800">
    <!-- sidebar head -->
    <div class="sidebar-head p-4">
        

          <img src="../../assets/img/logo-oscuro.png"  id="logo-image-black" class="visible dark:visible" style="width:12rem ;"  alt="" srcset="">
          <span
            class="bg-gray-700 absolute mt-2 dark:block hidden rounded-md py-1 px-2 text-xs text-gray-200"
            >Modo Oscuro</span
          >
      
      <button class="lg:hidden block float-right -mt-7" @click="sidebarToggle">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          aria-hidden="true"
          role="img"
          width="25px"
          height="25px"
          preserveAspectRatio="xMidYMid meet"
          viewBox="0 0 32 32"
        >
          <path
            fill="currentColor"
            d="M7.219 5.781L5.78 7.22L14.563 16L5.78 24.781l1.44 1.439L16 17.437l8.781 8.782l1.438-1.438L17.437 16l8.782-8.781L24.78 5.78L16 14.563z"
          />
        </svg>
      </button>
    </div>
    <!-- sidebar list -->
    <div class="sidebar-list p-4 mt-4" id="style-scroll-1">
      <p class="font-medium text-gray-400 dark:text-gray-600">Menu</p>
      <div class="wrap-item mt-4 dark:text-gray-500">
        <div class="item" >
          <router-link
            to="/app/alumno"
            exact
            id="InicioBtn"
            class="w-full flex text-left rounded-md box-border p-3 hover:bg-gray-100 dark:hover:bg-gray-700"
          >
            <span class="mr-3 text-xl dark:text-white"><Icon icon="ant-design:home-outlined" /></span>
            <span class="w-full dark:text-white"> Inicio </span>
          </router-link>
        </div>
         <div class="item">
          <router-link
            to="/"
            exact
            class="w-full flex text-left rounded-md box-border p-3 hover:bg-gray-100 dark:hover:bg-gray-700"
          >
            <span class="mr-3 text-xl text-black dark:text-white"><Icon icon="fluent:calendar-agenda-20-regular" /></span>
            <span class="w-full dark:text-white"> Agenda </span>
          </router-link>
        </div>

         <div class="item ">
          <router-link
            to="/"
            exact
            class="w-full flex text-left rounded-md box-border p-3 hover:bg-gray-100 dark:hover:bg-gray-700"
          >
            <span class="mr-3 text-xl text-black dark:text-white "><Icon icon="bx:time" /></span>
            <span class="w-full dark:text-white  "> Horario </span>
          </router-link>
        </div>
       
       <div class="item">
          <router-link
            to="/"
            exact
            class="w-full flex text-left rounded-md box-border p-3 hover:bg-gray-100 dark:hover:bg-gray-700"
          >
            <span class="mr-3 text-xl dark:text-white"><Icon icon="akar-icons:book-open" /></span>
            <span class="w-full dark:text-white"> Libro Digital </span>
          </router-link>
        </div>

         <div class="item">
          <router-link
            to="/"
            exact
            class="w-full flex text-left rounded-md box-border p-3 hover:bg-gray-100 dark:hover:bg-gray-700"
          >
            <span class="mr-3 text-xl dark:text-white"><Icon icon="ant-design:file-done-outlined" /></span>
            <span class="w-full dark:text-white"> Metas </span>
          </router-link>
        </div>

         <div class="item">
          <router-link
            to="/"
            exact
            class="w-full flex text-left rounded-md box-border p-3 hover:bg-gray-100 dark:hover:bg-gray-700"
          >
            <span class="mr-3 text-xl dark:text-white"><Icon icon="icon-park-outline:school" /></span>
            <span class="w-full dark:text-white"> Cursos </span>
          </router-link>
        </div>
        <div class="item">
          <router-link
            to="/"
            exact
            class="w-full flex text-left rounded-md box-border p-3 hover:bg-gray-100 dark:hover:bg-gray-700"
          >
            <span class="mr-3 text-xl dark:text-white"><Icon icon="tabler:school" /></span>
            <span class="w-full dark:text-white"> Asignatura </span>
          </router-link>
        </div>

         <div class="item">
          <router-link
            to="/"
            exact
            class="w-full flex text-left rounded-md box-border p-3 hover:bg-gray-100 dark:hover:bg-gray-700"
          >
            <span class="mr-3 text-xl dark:text-white"><Icon icon="carbon:warning" /></span>
            <span class="w-full dark:text-white"> Avisos </span>
          </router-link>
        </div>
      
      </div>
    

    

  
  
     
    </div>
  </nav>
</template>
<style>

</style>
<script>
  const html = document.querySelector("html");
  import { Icon } from "@iconify/vue";
  import MenuAccordion from "../MenuAccordion.vue";
  export default {
    components: {
      Icon,
      MenuAccordion,
    },
    methods: {
      sidebarToggle: function () {
        document.querySelector(".flex-sidebar").classList.add("hidden");
      },
    },
    mounted() {

     
    },
  };
</script>

<style>
#style-scroll-1::-webkit-scrollbar-track
{
	-webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
	border-radius: 10px;
	background-color: #F5F5F5;
}

#style-scroll-1::-webkit-scrollbar
{
	width: 12px;
	background-color: #F5F5F5;
}

#style-scroll-1::-webkit-scrollbar-thumb
{
	border-radius: 10px;
	-webkit-box-shadow: inset 0 0 6px rgba(0,0,0,.3);
	background-color: #6ec63b;
}
</style>
