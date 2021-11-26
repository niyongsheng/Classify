<template>

  <el-container>
    <el-header style="padding: 40px;">
      <div class="text-olive text-xxl">Recognize result</div>
    </el-header>
    <el-main style="background-color: #FFFFFF;">

      <el-row>
        <el-col :span="4" :offset="2" v-for="(item,index) in ClassList" :key="index">
          <div :class="index==channel?'divcss5':''">
            <el-card :body-style="{ padding: '0px' }">
              <img :src="item.url" class="image">
            </el-card>
          </div>
        </el-col>
      </el-row>

      <el-row style="padding-top: 3.125rem;">
        <el-alert
            title="Significance of garbage classification"
            type="success"
            description="1, reduce environmental pollution
By disposing of waste in landfills or piles,
It is also difficult to prevent the infiltration of harmful substances into the entire ecosystem as the earth circulates,
Pollution of water and land, through plants and animals, affects people's health.
2, save land resources
Landfills occupy land resources and cause serious erosion of land.
Reduce the amount of garbage by more than 60 percent by separating it and removing recyclable and non-degradable materials.
3, The use of renewable Resources Waste is caused by people's poor use of resources. Before garbage is disposed of, it is recycled through garbage sorting,
You can turn garbage into treasure.
4. Improve people's values
Garbage sorting can help people learn to save and use resources,
Develop good living habits and improve personal quality."
            :closable="false">
        </el-alert>
      </el-row>

      <el-row style="padding: 70px;">
        <el-col :span="18" :offset="7">
          <el-button type="danger" round @click="OpenMotor()">Open trash again</el-button>
          <el-button type="success" round @click="GoToPredict()">AI identify again</el-button>
        </el-col>
      </el-row>

    </el-main>
  </el-container>

</template>

<script>
var self
export default {
  data() {
    return {
      src: 'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg',
      channel: '',
      ClassList: [{
        url: 'static/image/1.png'
      }, {
        url: 'static/image/2.png'
      }, {
        url: 'static/image/3.png'
      }, {
        url: 'static/image/4.png'
      }]
    }
  },
  created: function () {
    this.channel = this.$route.params.channel
    this.OpenMotor()
    self = this
  },
  methods: {
    GoToPredict() {
      this.$router.push('./predict')
    },
    OpenMotor() {
      var channel = this.channel
      console.log('开始舵机')
      this.$notify({
        title: '垃圾桶通知',
        message: '垃圾桶即将打开',
        type: 'success'
      })
      this.$http.get('http://192.168.31.83:8080/open_motor?channel=' + channel, { // 还可以直接把参数拼接在url后边
      }).then(function (res) {
        // alert(res.data);
        self.$notify({
          title: '垃圾桶通知',
          message: '垃圾桶已经关闭'

        })
        console.log(res)
      }).catch(function (error) {
        console.log(error)
      })
    }
  }
}
</script>

<style>
.image {
  width: 100%;
  display: block;
}

.divcss5 {
  border: solid 10px #e54d42;
}
</style>
