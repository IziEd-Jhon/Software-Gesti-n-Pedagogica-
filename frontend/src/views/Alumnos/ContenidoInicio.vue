<template>
 <div class="card-page h-auto p-3">
    <nav class="flex" aria-label="Breadcrumb">
      <ol class="inline-flex items-center space-x-1 md:space-x-3">
        <li class="inline-flex items-center">
          <a
            href="#"
            class="inline-flex items-center text-sm font-medium text-gray-700 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white"
          >
        <Icon class="h-5 w-5 dark:text-white text-black mr-2" icon="ant-design:home-outlined" />

            Alumno
          </a>
        </li>
        <li>
          <div class="flex items-center">
            <svg
              class="w-6 h-6 text-gray-400"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                clip-rule="evenodd"
              ></path>
            </svg>
            <a
              href="#"
              class="ml-1 text-sm font-medium text-gray-700 hover:text-gray-900 md:ml-2 dark:text-gray-400 dark:hover:text-white"
              >Inicio</a
            >
          </div>
        </li>
     
      </ol>
    </nav>
    <!-- end nav -->
     <div class="mt-5 w-full">
      <h1 class="text-2xl text-gray-900 font-medium dark:text-gray-200">
        Pagina Alumno
      </h1>
      <p class="mt-1 text-sm font-normal text-gray-400">
         Donde podras ver la ultimas novedades de tu curso,compañeros y notificaciones de  profesores
      </p>
    </div>
    <div class="grid  lg:grid-cols-2 grid-cols-1 sm:grid-cols-1 md:grid-cols-2 gap-2 mt-5">
      <div class="card w-full p-5 rounded-md bg-white dark:bg-gray-800">

        <h2 class="dark:text-gray-200 flex ">
            <Icon icon="akar-icons:calendar" class="mr-2 mt-1" />Calendario</h2>
        <div class="wrapper-button w-full  mt-4">
          <div
            class="card p-6 max-w-sm bg-white rounded-lg border border-gray-200 shadow-md dark:bg-gray-800 dark:border-gray-700"
          >
            
            <Calendar   class="rounded-t-lg bg-white bg-black w-full" :attributes='attrs'></Calendar>
           
         
          </div>
        </div>
      </div>
      <div class="card w-full p-5 rounded-md bg-white dark:bg-gray-800">
        <h2 class="dark:text-gray-200">Horario</h2>
        <div class="wrapper-button w-full box-border mt-4">
          <div
            class="card max-w-sm bg-white rounded-lg border border-gray-200 shadow-md dark:bg-gray-800 dark:border-gray-700"
          >
               <app-accordion>
              <template v-slot:title> Lunes</template>
              <template v-slot:content>
             <div class="flex">
           <div class="flex-none w-1/2 h-full ">Lenguaje [202]</div>
           <div class="flex-none w-20">8:30-10:45</div>
           </div>
              <div class="flex">
           <div class="flex-none w-1/2 h-full ">Lenguaje [202]</div>
           <div class="flex-none w-20">8:30-10:45</div>
           </div>

              </template>
            </app-accordion>


            <app-accordion>
              <template v-slot:title> Martes</template>
              <template v-slot:content>
                 <div class="flex">
           <div class="flex-none w-1/2 h-full ">Lenguaje [202]</div>
           <div class="flex-none w-20">8:30-10:45</div>
           </div>
               <div class="flex">
           <div class="flex-none w-1/2 h-full ">Lenguaje [202]</div>
           <div class="flex-none w-20">8:30-10:45</div>
           </div>

              </template>
            </app-accordion>
         
            <app-accordion>
              <template v-slot:title> Miercoles</template>
              <template v-slot:content>
             <div class="flex">
                <div class="flex-none w-1/2 h-full ">Lenguaje [202]</div>
                <div class="flex-none w-20">8:30-10:45</div>
             </div>
             <div class="flex">
  <div class="flex-none w-full h-full dark:text-white">
    Lenguaje [202]
  </div>
  <div class="flex-none mr-2 dark:text-white">
    8:30-10:45
  </div>
 
</div>

              </template>
            </app-accordion>
            <app-accordion>
              <template v-slot:title> Jueves</template>
              <template v-slot:content>
             <div class="flex">
                <div class="flex-none w-1/2 h-full ">Lenguaje [202]</div>
                <div class="flex-none w-20">8:30-10:45</div>
             </div>
             <div class="flex">
                <div class="flex-none w-1/2 h-full ">Lenguaje [202]</div>
                <div class="flex-none w-20">8:30-10:45</div>
             </div>

              </template>
            </app-accordion>
            

            <app-accordion>
              <template v-slot:title> Viernes</template>
              <template v-slot:content>
             <div class="flex">
  <div class="flex-none w-full h-full dark:text-white">
    Lenguaje [202]
  </div>
  <div class="flex-none dark:text-white">
    8:30-10:45
  </div>
 
</div>
             <div class="flex">
  <div class="flex-none w-full h-full  dark:text-white">
    Lenguaje [202]
  </div>
  <div class="flex-none mr-2 dark:text-white">
    8:30-10:45
  </div>
 
</div>

              </template>
            </app-accordion>
          </div>
        </div>
      </div>
            <div class="card w-full p-5 rounded-md bg-white dark:bg-gray-800">
        <h2 class="dark:text-gray-200">Asistencia</h2>
        <div class="wrapper-button w-full box-border mt-4">
          <div
            class="card max-w-sm bg-white rounded-lg border border-gray-200 shadow-md dark:bg-white dark:border-gray-700"
          >
            <div  >
        <apexchart type="donut" :options="chartOptions" :series="series"></apexchart>
      </div>
              
          </div>
        </div>
      </div>

            <div class="card w-full p-5 rounded-md bg-white dark:bg-gray-800">
        <h2 class="dark:text-gray-200">Asistencia por Asignatura</h2>
        <div class="wrapper-button bg-white  w-full box-border mt-4">
      
        <apexchart type="bar"
         :options="chartOptionsBar" :series="seriesBar"
          
          ></apexchart>
        </div>
      </div>
    </div>
     

        <div
            class="danger-alert bg-red-500 py-3 px-5 text-white w-full box-border rounded-md"
          >
          <span class="text-2xl mr-5 flex">
              <Icon icon="bytesize:info" class="mr-2" />
              <span class="text-xl font-bold">Anuncios</span>

            </span>
            se publico una prueba de la asignatura de Lenguaje
          </div>
  </div>
</template>

<script>
import { Icon } from '@iconify/vue';
import {  Calendar,  } from 'v-calendar';
import AppAccordion from "../../components/AppAccordion.vue";
import VueApexCharts from 'vue-apexcharts'

import 'v-calendar/dist/style.css';
/*Documentacion Calendario  https://vcalendar.io/attributes.html*/


export default {
  name: "ContenidoInicio",
  components: {
    Icon,
    Calendar,
    AppAccordion,
    VueApexCharts
   },
  data() {
    
        
    return {

        /** Grafico Asistencia Por Asignatura */ 
        chartOptionsBar: {
            
            plotOptions: {
              bar: {
                borderRadius: 5,
                columnWidth: '50%',
              }
            },
            dataLabels: {
              enabled: false
            },
            stroke: {
              width: 2
            },
            
            grid: {
              row: {
                colors: ['#fff', '#f2f2f2']
              }
            },
            xaxis: {
              labels: {
                rotate: -45
              },
              categories: ['Ingles', 'Matematicas', 'Biologia', 'Lenguaje'
            
              ],
              tickPlacement: 'on'
            },
            yaxis: {
              title: {
                text: 'Clases Presente',
              },
            },
            fill: {
              type: 'gradient',
              gradient: {
                shade: 'light',
                type: "horizontal",
                shadeIntensity: 0.25,
                gradientToColors: undefined,
                inverseColors: true,
                opacityFrom: 0.85,
                opacityTo: 0.85,
                stops: [50, 0, 100]
              },
            }
          },

          seriesBar: [{
            name: 'Clases Presente',
            data: [44, 55, 41, 67]
          }],
          
          
        /** Grafico Asistencia **/
         optionsDonut: {
          chart: {
            type: "bar",
          },
          legend: false,
          dataLabels: {
            enabled: false,
          },
          labels: ["Ingles", "Matematicas", "Lenguaje", "Musica"],
        },
        seriesDonut: [20, 15, 63, 83],
         
       /** Marcar el dia de hoy en el calendario */
        attrs: [
        {
          key: 'today',
          highlight: 'green',
          dates: new Date(),
        },
      ],

       series: [ 55, 7, 15],
          chartOptions: {
            chart: {
              type: 'donut',
            },

            labels: ["Presente", "Justificado", "Ausente"],


            responsive: [{
              breakpoint: 480,
              options: {
                chart: {
                  width: 300
                },
                legend: {
                  position: 'bottom'
                }
              }
            }]
          },
      
    
    }
  },
  methods: {
   
  },
  mounted() {
  /**Boton inicio Fondo verde */
  document.getElementById("InicioBtn").style.backgroundColor='#6ec63b';
  
   
  }
}
</script>

<style scoped>
</style>