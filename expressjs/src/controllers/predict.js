`use strict`;

const tf = require('@tensorflow/tfjs');
const tfn = require("@tensorflow/tfjs-node");
const config = process.env;

const Predict = function(predict) {
    this.satisfaction_level = Number(predict.satisfaction_level);
    this.last_evaluation = Number(predict.last_evaluation);
    this.number_project = predict.number_project;
    this.average_montly_hours = predict.average_montly_hours;
    this.time_spend_company = predict.time_spend_company;
    this.work_accident = predict.work_accident;
    this.left = Number(predict.left);
    this.promotion_last_5years = Number(predict.promotion_last_5years);
    this.department_IT = conv_zero(predict.department_IT);
    this.department_RandD = conv_zero(predict.department_RandD);
    this.department_accounting = conv_zero(predict.department_accounting);
    this.department_hr = conv_zero(predict.department_hr);
    this.department_management = conv_zero(predict.department_management);
    this.department_marketing = conv_zero(predict.department_marketing);
    this.department_product_mng = conv_zero(predict.department_product_mng);
    this.department_sales = conv_zero(predict.department_sales);
    this.department_support = conv_zero(predict.department_support);
    this.department_technical = conv_zero(predict.department_technical);
    this.salary_level_high = conv_zero(predict.salary_level_high);
    this.salary_level_low = conv_zero(predict.salary_level_low);
    this.salary_level_medium = conv_zero(predict.salary_level_medium);
    this.get_values = function(){
        return [this.satisfaction_level, this.last_evaluation, this.number_project,
            this.average_montly_hours, this.time_spend_company, this.work_accident,
            this.promotion_last_5years, this.department_IT, this.department_RandD,
            this.department_accounting, this.department_hr, this.department_management,
            this.department_marketing, this.department_product_mng, this.department_sales,
            this.department_support, this.department_technical, this.salary_level_high,
            this.salary_level_low, this.salary_level_medium]
    }
}

function conv_zero(number)  {
    if(number == undefined) {return number = 0};
}

exports.predict = async (req, res) => {
    var { department, salary_level } = req.body;

    data = new Predict(req.body)

    switch(department){
        case "sales":
            data.department_sales = 1;
            break
        case "accounting":
            data.department_accounting = 1;
            break
        case "hr":
            data.department_hr = 1;
            break
        case "technical":
            data.department_technical = 1;
            break
        case "support":
            data.department_support = 1;
            break
        case "management":
            data.department_management = 1;
            break
        case "IT":
            data.department_IT = 1;
            break
        case "product_mng":
            data.department_product_mng = 1;
            break
        case "marketing":
            data.department_marketing = 1;
            break
    }

    switch(salary_level){
        case "low":
            data.salary_level_low = 1;
            break
        case "medium":
            data.salary_level_medium = 1;
            break
        case "high":
            data.salary_level_high = 1;
            break
    }
    console.log(tf.tensor(data.get_values()).print());
    const path_handler = tfn.io.fileSystem(process.env.MODEL_LAYER);
    const model = await tf.loadLayersModel(path_handler);
    // console.log("model", model)
    // const result = model.predict();
    // console.log("result", result);
    res.json({
        message: "data"
    });
};