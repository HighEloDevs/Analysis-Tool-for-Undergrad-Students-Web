<template>
  <v-simple-table dense>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">Parâmetro</th>
          <th class="text-left">Valor</th>
          <th class="text-left">Incerteza</th>
          <th class="text-right">Ações</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="param in data" :key="param.name">
          <td>{{ param.name }}</td>
          <td>{{ param.value }}</td>
          <td>{{ param.sigma }}</td>
          <td class="d-flex justify-end">
            <v-tooltip bottom>
              <template #activator="{ on, attrs }">
                <v-btn v-on="on" v-bind="attrs" icon small>
                  <v-icon small>fa-copy</v-icon>
                </v-btn>
              </template>
              Copiar
            </v-tooltip>
          </td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
</template>

<script>
export default {
  props: {
    data: {
      type: Array,
      default: () => []
    }
  }
}
</script>
