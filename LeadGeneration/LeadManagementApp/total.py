from django.shortcuts import render_template






def index():
  
    cursor = Connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM leadmanagementapp_calldetail")
    row_count = cursor.fetchone()[0]
    Connection.close()

    return render_template('AdminDashboard.html', row_count=row_count)


