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

            Profesor
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
        Pagina Profesor
      </h1>
      <p class="mt-1 text-sm font-normal text-gray-400">
         
      </p>
    </div>
    <div class="grid  lg:grid-cols-1 grid-cols-1 sm:grid-cols-1 md:grid-cols-2 gap-2 mt-5">
      <div class="card w-full p-5 rounded-md bg-white dark:bg-gray-800">

        <h2 class="dark:text-gray-200 flex ">
            <Icon icon="akar-icons:calendar" class="mr-2 mt-1" />Calendario</h2>
        <div class="wrapper-button w-full  mt-4">
          <div
            class="card p-2 max-w-md bg-white rounded-lg border border-gray-200 shadow-md dark:bg-gray-800 dark:border-gray-700"
          >
   <div class="text-center section">
    <Calendar
      class="custom-calendar max-w-full"
      :masks="masks"
      :attributes="attributes"
      disable-page-swipe
      is-expanded
    >
      <div
        slot="day-content"
        v-on="dayEvents"
        @click="dayClick"
        slot-scope="{ day, attributes }"
        class="flex flex-col h-full z-10 overflow-hidden"
        :class="day.year"
      >
        <span
          class="day-label text-sm text-gray-900"
          :class="[day.dateTime === today ? 'today rounded-sm' : '' ]"
        >{{ day.day }}</span>
        <div class="flex-grow overflow-y-scroll overflow-x-auto">
          <p
            v-for="attr in attributes"
            :key="attr.key"
            class="text-xs leading-tight rounded-sm p-1 mt-0 mb-1"
            :class="attr.customData.class"
          >{{ attr.customData.title }}</p>
        </div>
      </div>
    </Calendar>
  </div>
         
          </div>
        </div>
      </div>
          <div class="grid  lg:grid-cols-2 grid-cols-1 sm:grid-cols-1 md:grid-cols-2 gap-2 mt-5">

      <div class="card w-full p-5 rounded-md bg-white dark:bg-gray-800">
        <h2 class="dark:text-gray-200">Filtro</h2>
        <div class="wrapper-button w-full box-border mt-4">
          <div
            class="card max-w-md bg-white rounded-lg border border-gray-200 shadow-md dark:bg-gray-800 dark:border-gray-700"
          >
                  <h2 class=" w-50 bg-blue-100 bg-white border border-blue-200 hover:bg-blue-200 text-blue-600 rounded-l focus:bg-blue-500 focus:text-white focus:border-blue-500 focus:outline-none">Filtar por :</h2>


<select v-model="selected" class="w-full bg-blue-100 bg-white border border-blue-200 hover:bg-blue-200 text-blue-600 rounded-l focus:bg-blue-500 focus:text-white focus:border-blue-500 focus:outline-none">
  <option disabled value="">Selecciona una opcion</option>
  <option>Curso</option>
  <option>Asignatura</option>
</select>
<select v-model="selected2" class="w-full hidden bg-blue-100 bg-white border border-blue-200 hover:bg-blue-200 text-blue-600 rounded-l focus:bg-blue-500 focus:text-white focus:border-blue-500 focus:outline-none">
  <option disabled value="">Selecciona una opcion</option>
  <option>Historia</option>
  <option>Matematicas</option>
</select>
              <DatePicker class="inline-block h-full" v-model="datepicker">
    <template v-slot="{ inputValue, togglePopover }">
      <div class="flex items-center">
        <button
          class="p-2 bg-blue-100 bg-white border border-white outline-none hover:bg-blue-200 text-blue-600 rounded-l focus:bg-blue-500 focus:text-white focus:border-blue-500 focus:outline-none"
          @click="togglePopover()" 
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 20 20"
            class="w-4 h-4 fill-current"
          >
            <path
              d="M1 4c0-1.1.9-2 2-2h14a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V4zm2 2v12h14V6H3zm2-6h2v2H5V0zm8 0h2v2h-2V0zM5 9h2v2H5V9zm0 4h2v2H5v-2zm4-4h2v2H9V9zm0 4h2v2H9v-2zm4-4h2v2h-2V9zm0 4h2v2h-2v-2z"
            ></path>
          </svg>
        </button>
        <input
          :value="inputValue"
          class="bg-white text-gray-700 w-full py-1 px-2 appearance-none border rounded-r focus:outline-none focus:border-blue-500"
          readonly 
        />
      </div>
    </template>
  </DatePicker>

  
           
          </div>
        </div>
      </div>
            <div class="card w-full p-5 rounded-md bg-white dark:bg-gray-800">
        <h2 class="dark:text-gray-200">Hitos</h2>
        <div class="wrapper-button w-full box-border mt-4">
          <div
            class="card max-w-sm bg-white rounded-lg border border-gray-200 shadow-md dark:bg-white dark:border-gray-700"
          >
            <div  >
        <apexchart type="pie" :options="chartOptions" :series="series"></apexchart>
      </div>
              
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
        <apexchart type="pie" :options="chartOptions" :series="series"></apexchart>
      </div>
              
          </div>
        </div>
      </div>

            <div class="card w-full p-5 rounded-lg rounded-md bg-white dark:bg-gray-800">
        <h2 class="dark:text-gray-200">Asistencia por Asignatura</h2>
      
        <Bar class="bg-white"
    :chart-options="chartOptions"
    :chart-data="chartData"
    :chart-id="chartId"
    :dataset-id-key="datasetIdKey"
    :plugins="plugins"
    :width="width"
    :height="height"
  />
      </div>
    </div>
     
          <div class="card  p-5  rounded-md bg-white dark:bg-gray-800" >
            <h2 class="dark:text-gray-200 mb-2">Promedio Notas por curso</h2>

    <apexchart height="200" class="bg-white" type="line" :options="chartOptionsf" :series="seriesf"/>
          </div>
    </div>
       
 </div>
</template>

<script>
import { Icon } from '@iconify/vue';
import {  Calendar,DatePicker  } from 'v-calendar';

import AppAccordion from "../../../components/AppAccordion.vue";
import VueApexCharts from 'vue-apexcharts'
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, BarElement, CategoryScale, LinearScale } from 'chart.js'


import 'v-calendar/dist/style.css';
/*Documentacion Calendario  https://vcalendar.io/attributes.html*/
ChartJS.register(Title, Tooltip, BarElement, CategoryScale, LinearScale)

export const drills = [
  {
    id: 1,
    startTime: Date.now() - 1000 * 60 * 60 * 24 * 5,
    alertType: {
      id: 1,
      name: "Active Shooter",
      imageUrl: "https://static.preparedapp.com/ActiveShooter.png",
      tabColor: "orange"
    }
  },
  {
    id: 2,
    startTime: Date.now() - 1000 * 60 * 60 * 24 * 4,
    alertType: {
      id: 1,
      name: "Active Shooter",
      imageUrl: "https://static.preparedapp.com/ActiveShooter.png",
      tabColor: "orange"
    }
  },
  {
    id: 3,
    startTime: Date.now() - 1000 * 60 * 60 * 24 * 3,
    alertType: {
      id: 1,
      name: "Active Shooter",
      imageUrl: "https://static.preparedapp.com/ActiveShooter.png",
      tabColor: "orange"
    }
  }
];

export default {
  name: "ContenidoInicio",
  components: {
    Icon,
    Calendar,
    AppAccordion,
    VueApexCharts,
    Bar,
    DatePicker
    
    

   },
   props: {
    drills: {
      type: Array,
      default: () => [],
    },
  },


   props: {
    chartId: {
      type: String,
      default: 'bar-chart'
    },
    datasetIdKey: {
      type: String,
      default: 'label'
    },
    width: {
      type: Number,
      default: 300
    },
    height: {
      type: Number,
      default: 200
    },
    cssClasses: {
      default: '',
      type: String
    },
    styles: {
      type: Object,
      default: () => {}
    },
    plugins: {
     legend: {
      display: true,
       labels: {
                    font: {
                        size: 14,
                        family:"'Lexend', sans-serif ",
                        weight: "bold"
                    }
                    
                }
    }
    }
  },
  data() {
    const now = new Date();
    const month = now.getMonth();
    const year = now.getFullYear();
    const day = now.getDate();
        
    return {

       selected: '',
       selected2: '',

        datepicker: new Date(),
        /** Grafico Asistencia Por Asignatura */ 
       chartOptionsf: {
        xaxis: {
          type: "string",
          categories: [
            " 1 Medio A",
            " 1 Medio B",
            " 2 Medio A",
            " 3 Medio B",
            " 4 Medio B",
            " 3 Medio A"
          ]
        }
      
      },
      seriesf: [
        {
          name: "Promedio por curso",
          data: [ 4.2, 3.9, 5.8, 6.0, 4.0, 6.4]
        }
      ],
    
    
          /** Grafico Barras con la libreria vue3-chartjs y chartjs*/
            chartData: {
       labels: ['Ingles', 'Matematica', 'Toulon', 'Perpignan', 'Autre'],
      datasets: [
        {
          data: [30, 40, 60, 70, 5],
          backgroundColor: ['#E6B333', '#3366E6', '#999966', '#99FF99', '#B34D4D'],
        },
      ],
    },
    
          
          
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

         today: new Date()  ,
      masks: {
        weekdays: "WWW"
      },
      attributes: [
        {
          key: 1,
          customData: {
            title: "Lunch with mom.",
            class: "bg-red-600 text-white"
          },
          dates: new Date(2022, 6, 23)
        },
        {
          key: 2,
          customData: {
            title: "Take Noah to basketball practice",
            class: "bg-blue-500 text-white"
          },
          dates: new Date(year, month, 2)
        },
        {
          key: 3,
          customData: {
            title: "Noah's basketball game.",
            class: "bg-blue-500 text-white"
          },
          dates: new Date(year, month, 5)
        },
        {
          key: 4,
          customData: {
            title: "Take car to the shop",
            class: "bg-indigo-500 text-white"
          },
          dates: new Date(year, month, 5)
        },
        {
          key: 4,
          customData: {
            title: "Meeting with new client.",
            class: "bg-teal-500 text-white"
          },
          dates: new Date(year, month, 7)
        },
        {
          key: 5,
          customData: {
            title: "Mia's gymnastics practice.",
            class: "bg-pink-500 text-white"
          },
          dates: new Date(year, month, 11)
        },
        {
          key: 6,
          customData: {
            title: "Cookout with friends.",
            class: "bg-orange-500 text-white"
          },
          dates: { months: 5, ordinalWeekdays: { 2: 1 } }
        },
        {
          key: 7,
          customData: {
            title: "Mia's gymnastics recital.",
            class: "bg-pink-500 text-white"
          },
          dates: new Date(year, month, 22)
        },
        {
          key: 8,
          customData: {
            title: "Visit great grandma.",
            class: "bg-red-600 text-white"
          },
          dates: new Date(year, month, 25)
        },
        {
          key: "today",
          customData: {
            title: "Visit great grandma.",
            class: "bg-red-600 text-white"
          },
          dates: new Date()
        }
      ],
      dayEvents: {
        click: a => {
          // eslint-disable-next-line no-console
          console.log("dayEvents:", a);
        }
      }
    }
  },
   
  methods: {
    dayClick(a) {
      // eslint-disable-next-line no-console
      console.log("origin DOM click", a);
    }
  },
  mounted() {
  /**Boton inicio Fondo verde */
  document.getElementById("InicioBtn").style.backgroundColor='#6ec63b';
  
   
  }
}
</script>

<style>
.flex-col {
  flex-direction: column;
}

.flex {
  display: flex;
}
.flex-grow {
  flex-grow: 1;
}
.h-full {
  height: 100%;
}
.bg-red-600 {
  background-color: #e53e3e;
}
.today {
  background-color: #d2e1ec;
}
.bg-teal-500 {
  background-color: #38b2ac;
}
.bg-pink-500 {
  background-color: #ed64a6;
}
.bg-indigo-500 {
  background-color: #667eea;
}
.overflow-y-scroll {
  overflow-y: scroll;
}
.overflow-x-auto {
  overflow-x: auto;
}
.z-10 {
  z-index: 10;
}
.overflow-hidden {
  overflow: hidden;
}
.text-gray-900 {
  color: #1a202c;
}
.vc-h-full {
  height: 100%;
}
.custom-calendar.vc-container {
  --day-border: 1px solid #b8c2cc;
  --day-border-highlight: 1px solid #b8c2cc;
  --day-width: 90px;
  --day-height: 90px;
  --weekday-bg: #f8fafc;
  --weekday-border: 1px solid #eaeaea;
  border-radius: 0;
  width: auto;
}
.custom-calendar.vc-container .vc-weeks {
  padding: 0;
  height: 80vh;
  grid-template-rows: 33px repeat(6, 1fr);
}
.custom-calendar.vc-container .vc-header {
  background-color: #f1f5f8;
  padding: 10px 0;
}
.custom-calendar.vc-container .vc-weekday {
  background-color: var(--weekday-bg);
  border-bottom: var(--weekday-border);
  border-top: var(--weekday-border);
  padding: 5px 0;
}
.vc-border {
  border-width: 1px;
}
.custom-calendar.vc-container .vc-day:not(.on-right) {
  border-right: var(--day-border);
}
.custom-calendar.vc-container .vc-day:not(.on-bottom) {
  border-bottom: var(--day-border);
}
.custom-calendar.vc-container .vc-day.weekday-1,
.custom-calendar.vc-container .vc-day.weekday-7 {
  background-color: #eff8ff;
}

.custom-calendar.vc-container .vc-day {
  padding: 0 5px 3px;
  text-align: left;
  /*min-height: var(--day-height);*/
  min-width: var(--day-width);
  background-color: #fff;
}
.vc-day {
  position: relative;
  min-height: var(--day-min-height);
  width: 100%;
  height: 100%;
  z-index: 1;
}
.text-center {
  text-align: center;
}
.section {
}
.max-w-full {
  max-width: 100%;
}
.bg-blue-500 {
  background-color: #4299e1;
}

.text-xs {
  font-size: 0.75rem;
}
.text-white {
  color: #fff;
}
.p-1 {
  padding: 0.25rem;
}
.mb-1 {
  margin-bottom: 0.25rem;
}
.mt-0 {
  margin-top: 0;
}
.leading-tight {
  line-height: 1.25;
}
.rounded-sm {
  border-radius: 0.125rem;
}
::-webkit-scrollbar {
  width: 0px;
}
::-webkit-scrollbar-track {
  display: none;
}
</style>
