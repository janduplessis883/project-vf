html = """
<style>
.gradient-text {
    background: linear-gradient(45deg, #284d74, #d8ad45, #b2d9db, #e16d33);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    font-size: 48px;
    font-weight: bold;
}
</style>
<div class="gradient-text">INForcast</div>
"""


html2 = """
<style>
.gradient-text {
    background: linear-gradient(45deg, #284d74, #d8ad45, #b2d9db, #e16d33);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    font-size: 30px;
    font-weight: bold;
}
</style><div class="gradient-text">Historic Influenza vacc data (2000-2024)</div>"""


html3 = """
<style>
.gradient-text {
    background: linear-gradient(45deg, #284d74, #d8ad45, #b2d9db, #e16d33);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    font-size: 30px;
    font-weight: bold;
</style>
<div class="gradient-text">Influenza vacc Totals - 23/24</div>
"""


html4 = """
<style>
.gradient-text {
    background: linear-gradient(45deg, #284d74, #d8ad45, #b2d9db, #e16d33);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    font-size: 30px;
    font-weight: bold;
</style>
<div class="gradient-text">Quick Start Guide</div>
"""

quickguide = """Welcome to **INForcast**, never order too many vaccines again! 

**INForcast will help you forcast your next Influenza vaccine order**.

Leveraging advanced TimeSeries modeling, the app delves into historical vaccination records and seasonal patterns, offering you a tailored prediction for your future Influenza vaccine requirements. Moreover, we provide a comparative analysis of your current year’s vaccination statistics against the data from previous years, giving you a clearer picture of trends and changes.
Use our **trained model** to forcast your vaccination requirement, or train the model with your **own data**."""


html5 = """**Ready to get started?** 
    Upload your vaccination data, using the upload form. Data can be from SystmOne or Emis, as long as it is in the right format. [Download CSV templete](https://raw.githubusercontent.com/janduplessis883/project-inforcast/master/inforcast/sampledata/csv_template.csv).
    Download the [SystmOne Report Template](https://github.com/janduplessis883/project-inforcast/blob/master/images/INForcast-SystmOne-Search.rpt), import it to SystmOne Clinical Reporting and breakdown your search results by:"""


html6 = """Once you export this report to a CSV file, an extra column, `Patient Count`, will automatically be included.

    **Important**:
    >Please **update the format** of the 2 date columns, `Event date` and ` Date of Birth` as follows: 
    - Open the csv in Excel, select both columns and right click **Format Cells** 
    - Select CUSTOM and update the date format to `dd-mmm-yyyy`. Note you will need to type this as it is not selectable from the dorp-down list.

    To initiate the prediction, enter your practice's ODE code into the designated 'Practice Code' field and upload your CSV file. Our app will then dynamically illustrate your historical Influenza Vaccination data, emphasizing the figures from the previous year. Based on this, our model will project the quantity of vaccines your practice might need for the upcoming Influenza vaccination season.

    Embrace a smarter approach to vaccination planning with VaxPlanner 360."""

guide_code1 = """Vaccination Type
Event Date
Event Location ID
Patient Date of Birth"""
