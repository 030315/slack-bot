<template>
  <v-container fluid>
    <member-dialog ref="modal"></member-dialog>
    <v-layout row wrap>
      <v-btn color="info" @click="openCreate">新規作成</v-btn>
    </v-layout>
    <v-layout row wrap>
      <v-data-table
        :headers="headers"
        :items="items"
      >
        <template v-slot:items="props">
          <td>{{ props.item.fields.name1 + props.item.fields.name2 }}</td>
          <td>@{{ props.item.fields.slack_user_name }}</td>
          <td>{{ props.item.fields.clean_group_id }}</td>
        </template>
      </v-data-table>
    </v-layout>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Api from '@/Api';
import MemberDialog from '../components/Members/MemberDialog.vue';

interface Header {
  text: string,
  value: string,
}

interface Item {
  pk: number,
  model: string,
  fields: Fields
}

interface Fields {
  name1: string,
  name2: string,
  slack_user_name: string,
  clean_group_id: number,
}

@Component({
  components: {
    'member-dialog': MemberDialog
  },
})
export default class Members extends Vue {
  $refs: {
    'modal': MemberDialog
  }

  public headers: Header[] = [
    {text: '名前', value: 'name'},
    {text: 'Slackユーザーネーム', value: 'slack_user_name'},
    {text: '掃除グループ番号', value: 'clean_group_id'}
  ]

  public items?: Item[] = [];

  mounted() {
    this.getMembers();
  }

  /**
   * メンバー一覧の取得
   */
  public getMembers() {
    Api.get('/members/').then((data) => {
      this.items = data;
    }).catch((error) => {
      alert(error);
    });
  }

  public openCreate() {
    this.$refs.modal.open();
  }
}
</script>
