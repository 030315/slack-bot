<template>
  <v-navigation-drawer fixed clipped app>
    <v-toolbar flat>
      <v-list dense>
        <v-list-tile>
          <v-list-tile-title class="title">
            メニュー
          </v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-toolbar>
    <v-divider></v-divider>
    <v-list dense class="pt-0">
      <router-link
        :to="{name: item.to}"
        v-for="item in items"
        :key="item.title"
      >
        <v-list-tile>
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </router-link>
    </v-list>
  </v-navigation-drawer>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';

interface Item {
  title: string,
  icon: string,
  to: string
}

@Component
export default class Navigation extends Vue {
  public items: Item[] = [
    {
      title: 'メンバー一覧',
      icon: 'perm_identity',
      to: 'members'
    }
  ]
}

</script>


<style lang="scss" scoped>
a {
  text-decoration: none;
}
</style>
