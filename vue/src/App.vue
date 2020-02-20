<template>
  <v-app>
    <v-content>
      <v-container>
        <v-layout row wrap>
          <v-flex xs12>
            <Navigation />
            <router-view></router-view>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Navigation from './components/Navigation.vue';

@Component({
  components: {
    Navigation
  }
})
export default class App extends Vue {

}
</script>
