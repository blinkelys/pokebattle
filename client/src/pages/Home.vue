<template>
  <main class="min-h-screen overflow-hidden bg-slate-950 text-white">
    <!-- Background glow -->
    <div class="pointer-events-none fixed inset-0 overflow-hidden">
      <div
        class="absolute -left-40 -top-40 h-[500px] w-[500px] rounded-full bg-red-500/20 blur-[120px]"
      ></div>

      <div
        class="absolute right-[-150px] top-[30%] h-[500px] w-[500px] rounded-full bg-blue-500/20 blur-[120px]"
      ></div>

      <div
        class="absolute bottom-[-200px] left-[30%] h-[500px] w-[500px] rounded-full bg-yellow-400/10 blur-[120px]"
      ></div>
    </div>

    <!-- Hero -->
    <section class="relative mx-auto flex min-h-screen max-w-7xl items-center px-6 py-20 lg:px-12">
      <div class="grid w-full items-center gap-16 lg:grid-cols-2">
        <!-- Text -->
        <div class="relative z-10">


          <h1
            class="text-6xl font-black uppercase leading-[0.9] tracking-tighter sm:text-7xl lg:text-8xl"
          >
            Welcome to
            <span
              class="block bg-gradient-to-r from-red-500 via-yellow-400 to-blue-500 bg-clip-text text-transparent"
            >
              Pokebattles
            </span>
          </h1>

          <p class="mt-8 max-w-xl text-lg leading-relaxed text-slate-300 sm:text-xl">
            Choose your Pokémon. Build your team. Master the battlefield.
            <span class="font-bold text-white">Your next battle starts here.</span>
          </p>

          <!-- Buttons -->
          <div class="mt-10 flex flex-wrap gap-4">
            <router-link
              to="/battle"
              class="group relative overflow-hidden rounded-2xl bg-red-500 px-8 py-4 font-black uppercase tracking-wider shadow-2xl shadow-red-500/30 transition duration-300 hover:-translate-y-1 hover:bg-red-400 hover:shadow-red-500/50"
            >
              <span class="relative z-10 flex items-center gap-3">
                ⚔️ Enter Battle
                <span class="transition-transform duration-300 group-hover:translate-x-1">
                  →
                </span>
              </span>

              <div
                class="absolute inset-0 -translate-x-full bg-white/20 transition-transform duration-500 group-hover:translate-x-full"
              ></div>
            </router-link>

            <router-link
              to="/pokemons"
              class="rounded-2xl border border-white/20 bg-white/5 px-8 py-4 font-black uppercase tracking-wider backdrop-blur transition duration-300 hover:-translate-y-1 hover:border-yellow-400/50 hover:bg-yellow-400/10 hover:text-yellow-300"
            >
              Browse Pokémon
            </router-link>
          </div>

          <!-- Quick stats -->
          <div class="mt-12 flex flex-wrap gap-8 border-t border-white/10 pt-8">
            <div>
              <p class="text-3xl font-black text-yellow-400">151+</p>
              <p class="text-xs font-bold uppercase tracking-widest text-slate-500">
                Pokémon
              </p>
            </div>

            <div>
              <p class="text-3xl font-black text-red-400">∞</p>
              <p class="text-xs font-bold uppercase tracking-widest text-slate-500">
                Battles
              </p>
            </div>
          </div>
        </div>

        <!-- Hero Pokémon artwork -->
        <div class="relative flex items-center justify-center">
          <!-- Rings -->
          <div
            class="absolute h-[420px] w-[420px] rounded-full border border-white/10"
          ></div>

          <div
            class="absolute h-[340px] w-[340px] rounded-full border border-yellow-400/20"
          ></div>

          <div
            class="absolute h-[260px] w-[260px] rounded-full bg-red-500/10 blur-2xl"
          ></div>

          <!-- Images -->
          <img
            src="../assets/home1.png"
            alt=""
            class="relative z-20 w-[70%] max-w-md drop-shadow-[0_30px_40px_rgba(0,0,0,0.7)] transition duration-500 hover:scale-105"
          />

          <img
            src="../assets/home2.png"
            alt=""
            class="absolute -right-2 top-8 z-10 w-32 rotate-12 drop-shadow-2xl transition duration-500 hover:rotate-6"
          />

          <img
            src="../assets/home3.png"
            alt=""
            class="absolute -bottom-4 -left-2 z-10 w-36 -rotate-12 drop-shadow-2xl transition duration-500 hover:-rotate-6"
          />
        </div>
      </div>
    </section>

    <!-- Game modes -->
    <section class="relative mx-auto max-w-7xl px-6 py-24 lg:px-12">
      <div class="mb-12">
        <p class="mb-3 text-sm font-black uppercase tracking-[0.3em] text-red-400">
          Choose your path
        </p>

        <h2 class="text-4xl font-black tracking-tight sm:text-5xl">
          Everything you need to
          <span class="text-yellow-400">battle.</span>
        </h2>
      </div>

      <div class="grid gap-6 md:grid-cols-3">
        <!-- Battle -->
        <router-link
          to="/battle"
          class="group relative overflow-hidden rounded-3xl border border-red-500/20 bg-gradient-to-br from-red-500/20 to-slate-900 p-8 transition duration-300 hover:-translate-y-2 hover:border-red-400/60 hover:shadow-2xl hover:shadow-red-500/20"
        >
          <div
            class="absolute -right-10 -top-10 h-40 w-40 rounded-full bg-red-500/20 blur-3xl transition group-hover:bg-red-500/40"
          ></div>

          <div class="relative">
            <div class="mb-6 text-5xl">⚔️</div>

            <h3 class="text-2xl font-black">
              Battle Arena
            </h3>

            <p class="mt-3 text-slate-400">
              Put your team to the test and prove your skills in battle.
            </p>

            <div class="mt-6 font-bold text-red-400">
              ENTER ARENA →
            </div>
          </div>
        </router-link>

        <!-- Pokémon -->
        <router-link
          to="/pokemons"
          class="group relative overflow-hidden rounded-3xl border border-blue-500/20 bg-gradient-to-br from-blue-500/20 to-slate-900 p-8 transition duration-300 hover:-translate-y-2 hover:border-blue-400/60 hover:shadow-2xl hover:shadow-blue-500/20"
        >
          <div
            class="absolute -right-10 -top-10 h-40 w-40 rounded-full bg-blue-500/20 blur-3xl transition group-hover:bg-blue-500/40"
          ></div>

          <div class="relative">
            <div class="mb-6 text-5xl">🔵</div>

            <h3 class="text-2xl font-black">
              Pokémon
            </h3>

            <p class="mt-3 text-slate-400">
              Explore Pokémon, discover their abilities, and build your team.
            </p>

            <div class="mt-6 font-bold text-blue-400">
              VIEW POKÉMON →
            </div>
          </div>
        </router-link>

        <!-- About -->
        <router-link
          to="/about"
          class="group relative overflow-hidden rounded-3xl border border-yellow-500/20 bg-gradient-to-br from-yellow-500/20 to-slate-900 p-8 transition duration-300 hover:-translate-y-2 hover:border-yellow-400/60 hover:shadow-2xl hover:shadow-yellow-500/20"
        >
          <div
            class="absolute -right-10 -top-10 h-40 w-40 rounded-full bg-yellow-500/20 blur-3xl transition group-hover:bg-yellow-500/40"
          ></div>

          <div class="relative">
            <div class="mb-6 text-5xl">📖</div>

            <h3 class="text-2xl font-black">
              About
            </h3>

            <p class="mt-3 text-slate-400">
              Learn more about Pokebattles and how the game works.
            </p>

            <div class="mt-6 font-bold text-yellow-400">
              LEARN MORE →
            </div>
          </div>
        </router-link>
      </div>
    </section>

    <!-- Trainer -->
    <section class="relative mx-auto max-w-7xl px-6 pb-32 lg:px-12">
      <div
        class="relative overflow-hidden rounded-[2rem] border border-white/10 bg-gradient-to-br from-slate-900 via-slate-900 to-blue-950"
      >
        <!-- Background effects -->
        <div
          class="absolute right-0 top-0 h-full w-1/2 bg-blue-500/10 blur-3xl"
        ></div>

        <div
          class="absolute bottom-0 left-0 h-64 w-64 rounded-full bg-red-500/10 blur-3xl"
        ></div>

        <div class="relative grid items-center gap-12 p-8 sm:p-12 lg:grid-cols-2 lg:p-16">
          <!-- Trainer image -->
          <div class="order-2 flex justify-center lg:order-1">
            <div class="relative">
              <div
                class="absolute inset-0 rounded-full bg-blue-500/20 blur-3xl"
              ></div>

              <img
                src="../assets/homeTrainer.png"
                alt="Pokémon Trainer"
                class="relative z-10 max-h-[500px] w-auto drop-shadow-[0_30px_30px_rgba(0,0,0,0.6)] transition duration-500 hover:-translate-y-3"
              />
            </div>
          </div>

          <!-- Text -->
          <div class="order-1 relative z-10 lg:order-2">
            <p class="text-sm font-black uppercase tracking-[0.3em] text-blue-400">
              Your adventure awaits
            </p>

            <h2 class="mt-4 text-5xl font-black tracking-tight">
              Meet your
              <span class="text-yellow-400">Trainer.</span>
            </h2>

            <p class="mt-6 text-lg leading-relaxed text-slate-400">
              Your trusty trainer is ready to guide you through the world of
              Pokebattles. Learn the mechanics, prepare your team, and step
              into the arena.
            </p>

            <button
              class="mt-8 rounded-2xl bg-white px-7 py-4 font-black uppercase tracking-wider text-slate-950 transition duration-300 hover:-translate-y-1 hover:bg-yellow-400"
            >
              How to Battle →
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="border-t border-white/10 px-6 py-8 text-center">
      <p class="text-sm font-bold text-slate-600">
        POKEBATTLES
        <span class="mx-2">•</span>
        Gotta battle 'em all.
      </p>
    </footer>
  </main>
</template>