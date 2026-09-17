<template>
  <main class="min-h-screen overflow-hidden bg-slate-950 text-white">
    <!-- Background effects -->
    <div class="pointer-events-none fixed inset-0 overflow-hidden">
      <div
        class="absolute -left-40 -top-40 h-[500px] w-[500px] rounded-full bg-red-500/10 blur-[120px]"
      ></div>

      <div
        class="absolute -right-40 top-[25%] h-[500px] w-[500px] rounded-full bg-blue-500/10 blur-[120px]"
      ></div>

      <div
        class="absolute bottom-[-200px] left-[35%] h-[500px] w-[500px] rounded-full bg-yellow-400/10 blur-[120px]"
      ></div>
    </div>

    <!-- Header -->
    <section class="relative mx-auto max-w-7xl px-6 pb-10 pt-20 lg:px-12">
      <div class="flex flex-col gap-8 md:flex-row md:items-end md:justify-between">
        <div>
          <div
            class="mb-5 inline-flex items-center gap-2 rounded-full border border-blue-400/30 bg-blue-400/10 px-4 py-2 text-sm font-bold uppercase tracking-[0.25em] text-blue-300 backdrop-blur"
          >
            <span class="h-2 w-2 animate-pulse rounded-full bg-blue-400"></span>
            Pokédex
          </div>

          <h1
            class="text-5xl font-black uppercase tracking-tighter sm:text-6xl lg:text-7xl"
          >
            Pokémon
            <span
              class="bg-gradient-to-r from-red-500 via-yellow-400 to-blue-500 bg-clip-text text-transparent"
            >
              Database
            </span>
          </h1>

          <p class="mt-5 max-w-2xl text-lg text-slate-400">
            Explore Pokémon, their stats, abilities, moves and battle types.
          </p>
        </div>

        <!-- Search -->
        <div class="w-full md:w-80">
          <label
            for="pokemon-search"
            class="mb-2 block text-xs font-black uppercase tracking-[0.2em] text-slate-500"
          >
            Search Pokémon
          </label>

          <div class="relative">
            <span
              class="pointer-events-none absolute left-4 top-1/2 -translate-y-1/2 text-xl"
            >
              🔎
            </span>

            <input
              id="pokemon-search"
              v-model="search"
              type="text"
              placeholder="Search by name..."
              class="w-full rounded-2xl border border-white/10 bg-white/5 py-4 pl-12 pr-5 font-semibold text-white outline-none backdrop-blur-xl transition placeholder:text-slate-600 focus:border-yellow-400/50 focus:bg-white/10 focus:ring-2 focus:ring-yellow-400/10"
            />
          </div>
        </div>
      </div>
    </section>

    <!-- Pokémon count -->
    <section class="relative mx-auto max-w-7xl px-6 pb-8 lg:px-12">
      <div class="flex items-center justify-between">
        <p class="text-sm font-bold uppercase tracking-widest text-slate-500">
          Showing
          <span class="text-white">{{ filteredPokemons.length }}</span>
          Pokémon
        </p>

        <p class="hidden text-sm font-bold uppercase tracking-widest text-slate-600 sm:block">
          Sorted by Pokédex ID
        </p>
      </div>
    </section>

    <!-- Pokémon grid -->
    <section class="relative mx-auto max-w-7xl px-6 pb-32 lg:px-12">
      <div
        v-if="filteredPokemons.length"
        class="grid gap-6 md:grid-cols-2 lg:grid-cols-3"
      >
        <article
          v-for="pokemon in filteredPokemons"
          :key="pokemon.id"
          class="group relative overflow-hidden rounded-[2rem] border border-white/10 bg-slate-900/80 shadow-2xl backdrop-blur-xl transition duration-300 hover:-translate-y-2 hover:border-white/20"
        >
          <!-- Card glow -->
          <div
            class="absolute -right-20 -top-20 h-48 w-48 rounded-full bg-blue-500/10 blur-3xl transition duration-500 group-hover:bg-blue-500/20"
          ></div>

          <!-- Top section -->
          <div class="relative overflow-hidden px-6 pb-4 pt-6">
            <div class="flex items-start justify-between">
              <!-- ID -->
              <span
                class="rounded-full border border-white/10 bg-white/5 px-3 py-1 text-xs font-black tracking-widest text-slate-500"
              >
                #{{ String(pokemon.id).padStart(3, '0') }}
              </span>

              <!-- Types -->
              <div class="flex gap-2">
                <span
                  v-for="type in pokemon.types"
                  :key="type"
                  class="rounded-full border border-white/10 bg-white/5 px-3 py-1 text-xs font-black uppercase tracking-wider text-slate-300"
                >
                  {{ type }}
                </span>
              </div>
            </div>

            <!-- Sprite -->
            <div class="relative mx-auto flex h-56 items-center justify-center">
              <div
                class="absolute h-40 w-40 rounded-full bg-blue-500/10 blur-3xl transition duration-500 group-hover:scale-125"
              ></div>

              <img
                :src="getSprite(pokemon)"
                :alt="pokemon.name"
                class="relative z-10 h-48 w-48 object-contain drop-shadow-[0_20px_20px_rgba(0,0,0,0.6)] transition duration-500 group-hover:scale-110"
              />
            </div>

            <!-- Name -->
            <div class="text-center">
              <h2
                class="text-3xl font-black capitalize tracking-tight"
              >
                {{ pokemon.name }}
              </h2>

              <div class="mt-2 flex justify-center gap-4 text-xs font-bold uppercase tracking-widest text-slate-500">
                <span>Height {{ pokemon.height }}</span>
                <span>Weight {{ pokemon.weight }}</span>
              </div>
            </div>
          </div>

          <!-- Stats -->
          <div class="border-t border-white/10 px-6 py-5">
            <div class="mb-4 flex items-center justify-between">
              <h3 class="text-xs font-black uppercase tracking-[0.2em] text-slate-500">
                Base Stats
              </h3>

              <span class="text-xs font-bold text-yellow-400">
                {{ totalStats(pokemon.stats) }} TOTAL
              </span>
            </div>

            <div class="space-y-3">
              <div
                v-for="(value, stat) in pokemon.stats"
                :key="stat"
              >
                <div class="mb-1 flex justify-between text-xs font-bold">
                  <span class="uppercase text-slate-500">
                    {{ formatStatName(stat) }}
                  </span>

                  <span class="text-white">
                    {{ value }}
                  </span>
                </div>

                <div class="h-1.5 overflow-hidden rounded-full bg-white/5">
                  <div
                    class="h-full rounded-full bg-gradient-to-r from-red-500 via-yellow-400 to-blue-500 transition-all duration-700 group-hover:brightness-125"
                    :style="{ width: `${Math.min((value / 255) * 100, 100)}%` }"
                  ></div>
                </div>
              </div>
            </div>
          </div>

          <!-- Abilities -->
          <div class="border-t border-white/10 px-6 py-5">
            <h3 class="mb-3 text-xs font-black uppercase tracking-[0.2em] text-slate-500">
              Abilities
            </h3>

            <div class="flex flex-wrap gap-2">
              <span
                v-for="ability in pokemon.abilities"
                :key="ability"
                class="rounded-xl border border-yellow-400/10 bg-yellow-400/5 px-3 py-2 text-sm font-bold capitalize text-yellow-300"
              >
                {{ ability }}
              </span>
            </div>
          </div>

          <!-- Moves -->
          <div class="border-t border-white/10 px-6 py-5">
            <div class="flex items-center justify-between">
              <h3 class="text-xs font-black uppercase tracking-[0.2em] text-slate-500">
                Moves
              </h3>

              <span class="text-xs font-bold text-slate-600">
                {{ pokemon.moves?.length ?? 0 }}
              </span>
            </div>

            <div class="mt-3 flex flex-wrap gap-2">
              <span
                v-for="move in pokemon.moves?.slice(0, 6)"
                :key="move"
                class="rounded-lg bg-white/5 px-2.5 py-1.5 text-xs font-semibold capitalize text-slate-400 transition hover:bg-white/10 hover:text-white"
              >
                {{ move }}
              </span>

              <span
                v-if="pokemon.moves?.length > 6"
                class="rounded-lg bg-white/5 px-2.5 py-1.5 text-xs font-bold text-slate-600"
              >
                +{{ pokemon.moves.length - 6 }} more
              </span>
            </div>
          </div>
        </article>
      </div>

      <!-- Empty state -->
      <div
        v-else
        class="flex min-h-[400px] flex-col items-center justify-center rounded-[2rem] border border-white/10 bg-white/[0.02] text-center"
      >
        <div class="text-7xl">🔎</div>

        <h2 class="mt-6 text-3xl font-black">
          No Pokémon found
        </h2>

        <p class="mt-3 text-slate-500">
          Try searching for another Pokémon name.
        </p>

        <button
          class="mt-6 rounded-xl bg-white/5 px-5 py-3 text-sm font-black uppercase tracking-wider transition hover:bg-white/10"
          @click="search = ''"
        >
          Clear Search
        </button>
      </div>
    </section>
  </main>
</template>

<script setup>
import { computed, ref } from 'vue'
import api from '../api'

// Replace this with your API/store data.
const pokemons = ref([])

api.get('/all-pokemons').then(response => {
  pokemons.value = response.data.pokemons
})

const search = ref('')

const filteredPokemons = computed(() => {
  return [...pokemons.value]
    .filter((pokemon) =>
      pokemon.name
        .toLowerCase()
        .includes(search.value.toLowerCase().trim())
    )
    .sort((a, b) => a.id - b.id)
})

function getSprite(pokemon) {
  if (typeof pokemon.sprites === 'string') {
    return pokemon.sprites
  }

  return (
    pokemon.sprites?.front_default ||
    pokemon.sprites?.other?.['official-artwork']?.front_default ||
    ''
  )
}

function totalStats(stats) {
  if (!stats) return 0

  return Object.values(stats).reduce(
    (total, value) => total + Number(value),
    0
  )
}

function formatStatName(stat) {
  const names = {
    hp: 'HP',
    attack: 'Attack',
    defense: 'Defense',
    'special-attack': 'Sp. Attack',
    'special-defense': 'Sp. Defense',
    speed: 'Speed',
  }

  return names[stat] || stat.replaceAll('-', ' ')
}
</script>
