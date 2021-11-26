/* eslint-disable */
<template>
  <div style="background-color: #FFFFFF;">

    <el-row style="padding: 22px;">
      <el-col :span="12">
        <el-card class="box-card" :body-style="{ padding: '0px', height: '60%'}">
          <img src="http://192.168.31.83:8080/video_img_url" class="image"></img>
        </el-card>
      </el-col>
      <el-col :span="8" :offset="2">
        <img src="static/image/main_icon.png" class="image"></img>
        <el-col :offset="5">
          <el-button type="success" round style="margin-top: 30px" @click="takeAPhotho()">
            <i class="el-icon-camera"> AI Classify</i>
          </el-button>
        </el-col>
      </el-col>
    </el-row>

    <el-steps :active="3" align-center style="padding: 40px;">
      <el-step title="Step1" description="Place sorted garbage at the correct location on the platform"></el-step>
      <el-step title="Step2"
               description="Click the take a picture button and wait for the AI recognition result"></el-step>
      <el-step title="Step3"
               description="Machine identification success, waiting to open the corresponding trash can"></el-step>
    </el-steps>

  </div>

</template>

<script>
var self
export default {
  data() {
    return {
      src: 'https://likecy.oss-cn-beijing.aliyuncs.com/0194a25dcd1b46a8012053c074fa37.jpg@2o_1574846777533.jpg'
    }
  },
  created: function () {
    self = this
  },
  methods: {
    GoToResult() {
      this.$router.push('./result')
    },
    takeAPhotho() {
      self.$router.push({
        name: 'result',
        params: {
          channel: 0
        }
      })

      this.$http.get('http://192.168.31.83:8080/shut_photho', { // 还可以直接把参数拼接在url后边
      }).then(function (res) {
        self.$message({
          message: res.data,
          type: 'success'
        })
        self.deltailDataFromServers(res.data)
        console.log(res)
      }).catch(function (error) {
        console.log(error)
      })
    },
    deltailDataFromServers(data) {
      var result = data.split('/')
      switch (result[0]) {
        case '可回收物':
          self.$router.push({
            name: 'result',
            params: {
              channel: 0
            }
          })
          break
        case '其他垃圾':
          self.$router.push({
            name: 'result',
            params: {
              channel: 1
            }
          })
          break
        case '厨余垃圾':
          self.$router.push({
            name: 'result',
            params: {
              channel: 2
            }
          })
          break
        case '有害垃圾':
          self.$router.push({
            name: 'result',
            params: {
              channel: 3
            }
          })
          break
      }
    }
  }
}
</script>

<style>
.image {
  width: 50%;
  height: 60%;
}

</style>
