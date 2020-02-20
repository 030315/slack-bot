<template>
  <v-dialog persistent v-model="dialog" max-width="600px">
    <v-card>
      <v-card-title>
        <span class="headline">ユーザー登録</span>
      </v-card-title>
      <v-card-text>
        <v-container fluid>
          <v-layout wrap>
            <v-flex xs6>
              <v-text-field label="姓"></v-text-field>
            </v-flex>
            <v-flex xs6>
              <v-text-field label="名"></v-text-field>
            </v-flex>
          </v-layout>
          <v-layout wrap>
            <v-flex xs12>
              <v-text-field label="Slackユーザー名"></v-text-field>
            </v-flex>
          </v-layout>
          <v-layout wrap>
            <v-flex xs12>
              <v-select
                label="掃除グループ番号"
                :items="clean_groups"
              ></v-select>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-btn color="danger" @click="close">キャンセル</v-btn>
        <v-btn color="success" @click="save">登録</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator';
import Api from '@/Api';

interface inputs {
  name1: string,
  name2: string,
  slack_user_name: string,
  clean_group_id: number
}

@Component
export default class MemberDialog extends Vue {
  public dialog: Boolean = false;
  public clean_groups:String[] = ['1', '2', '3', '4']

  public inputs: inputs

  public save() {
    Api.post('/members/add', this.inputs).then((data) => {

    }).catch((error) => {

    });

    this.close();
  }

  public open() {
    this.dialog = true;
  }

  public close() {
    this.dialog = false;
  }
}
</script>

