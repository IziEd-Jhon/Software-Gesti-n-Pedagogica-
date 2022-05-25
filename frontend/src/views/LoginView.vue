<template>
  <div>
    <body class="bg-dark">
      <section>
        <div class="row g-0">
          <div class="col-lg-7 d-none d-lg-block">
            <div
              id="carouselExampleCaptions"
              class="carousel slide"
              data-ride="carousel"
            >
              <ol class="carousel-indicators">
                <li
                  data-target="#carouselExampleCaptions"
                  data-slide-to="0"
                  class="active"
                ></li>
                <li
                  data-target="#carouselExampleCaptions"
                  data-slide-to="1"
                ></li>
              </ol>
              <div class="carousel-inner">
                <div class="carousel-item img-1 min-vh-100 active">
                  <div class="carousel-caption d-none d-md-block"></div>
                </div>
                <div class="carousel-item img-2 min-vh-100">
                  <div class="carousel-caption d-none d-md-block"></div>
                </div>
              </div>
              <a
                class="carousel-control-prev"
                href="#carouselExampleCaptions"
                role="button"
                data-slide="prev"
              >
                <span
                  class="carousel-control-prev-icon"
                  aria-hidden="true"
                ></span>
                <span class="sr-only">Previous</span>
              </a>
              <a
                class="carousel-control-next"
                href="#carouselExampleCaptions"
                role="button"
                data-slide="next"
              >
                <span
                  class="carousel-control-next-icon"
                  aria-hidden="true"
                ></span>
                <span class="sr-only">Next</span>
              </a>
            </div>
          </div>

          <div
            class="col-lg-5 bg-dark d-flex flex-column align-items-end min-vh-100"
          >
            <div
              class="align-self-center px-lg-4 pt-lg-4 pb-lg-3 p-4 mb-auto w-100"
            >
              <img src="../assets/img/logo-izied-05.png" class="img-fluid" />
            </div>
            <div class="align-self-center w-100 px-lg-5 py-lg-4 p-2">
              <h1 class="font-weight-bold mb-2" style="font-size: 35px ;">Bienvenido de vuelta</h1>
              <form class="mb-5">
                <div class="mb-4">
                  <label
                    for="exampleInputEmail1"
                    class="form-label font-weight-bold"
                    >Email</label
                  >
                  <input
                    type="email"
                    class="form-control bg-dark-x border-0"
                    id="exampleInputEmail1"
                    placeholder="Ingresa tu email"
                    aria-describedby="emailHelp"
                  />
                </div>
                <div class="mb-4">
                  <label
                    for="exampleInputPassword1"
                    class="form-label font-weight-bold"
                    >Contraseña</label
                  >
                  <input
                    type="password"
                    class="form-control bg-dark-x border-0 mb-2"
                    placeholder="Ingresa tu contraseña"
                    id="exampleInputPassword1"
                  />
                  <a
                    href=""
                    id="emailHelp"
                    class="form-text text-muted text-decoration-none"
                    >¿Has olvidado tu contraseña?</a
                  >
                </div>

                <!-- Boton con siguiente pagina -->

                <router-link to="/app/homepage" v-slot="{ href, navigate }">
                  <button
                    :href="href"
                    @click="navigate"
                    type="submit"
                    class="btn btn-primary w-100"
                  >
                    Iniciar sesión
                  </button>
                </router-link>
              </form>

              <p class="font-weight-bold text-center text-muted">
                O inicia sesión con
              </p>
              <div class="d-flex justify-content-around">
                <button
                  type="button"
                  class="btn btn-outline-light flex-grow-1 mr-2"
                >
                  <i class="fab fa-google lead mr-2"></i> Google
                </button>
                <button
                  type="button"
                  class="btn btn-outline-light flex-grow-1 ml-2"
                >
                  <i class="fab fa-facebook-f lead mr-2"></i> Facebook
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>
    </body>
  </div>
</template>

<script>
export default {
  mounted() {},
};
</script>

<style>
:root {
  --dark: #16191c;
  --dark-x: #1e2126;
  --light: #ffffff;
}

.text-light {
  color: var(--light) !important;
}
.bg-dark {
  background-color: var(--dark) !important;
}
.bg-dark-x {
  background-color: var(--dark-x);
}

.btn {
  min-height: 3.125rem;
  font-weight: 600;
}

.form-control {
  min-height: 3.15rem;
  line-height: initial;
}
.form-control:focus {
  background-color: var(--dark-x);
  outline: none;
}

.btn-primary {
  background-color: #6ec63b;
  border-color: #6ec63b;
}

.min-vh-100 {
  min-height: 120vh !important;
}

.btn-primary:hover {
  background-color: #5ea735;
  border-color: #5ea735;
}

.text-light {
  color: var(--light) !important;
}
.bg-dark {
  background-color: var(--dark) !important;
  font-family: "Spartan", sans-serif;
  font-weight: 300;
  color: var(--light);
}
.bg-dark-x {
  background-color: var(--dark-x);
}

.btn {
  min-height: 3.125rem;
  font-weight: 600;
}

.form-control {
  min-height: 3.125rem;
  line-height: initial;
}
.form-control:focus {
  background-color: var(--dark-x);
  outline: none;
}

.img-1 {
  background-image: url("https://images.unsplash.com/photo-1580582932707-520aed937b7b?crop=entropy&cs=tinysrgb&fm=jpg&ixlib=rb-1.2.1&q=80&raw_url=true&ixid=4QpaYYb8YvXtaNjz81Xjt34m1PaHLNFU3oQxEXn9LZcY&auto=format&fit=crop&w=1032");
  background-size: cover;
  background-position: center;
}

.img-2 {
  background-image: url("https://images.unsplash.com/photo-1509062522246-3755977927d7?ixlib=rb-1.2.1&raw_url=true&q=80&fm=jpg&crop=entropy&cs=tinysrgb&ixid=4QpaYYb8YvXtaNjz81Xjt34m1PaHLNFU3oQxEXn9LZcY&auto=format&fit=crop&w=932");
  background-size: cover;
  background-position: center;
}

.img-fluid {
  height: 70px;
}
</style>
