<head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>

<h1>Patient List</h1>
<p>Build with Python using Bottle and Firestore</p>
<table>
    %setdefault('icategory', '')
    <tr>
        <th>Age</th>
        <th>Diagonosis</th>
        <th>Medication</th>
        <th>Name</th>
        <th>Therapy Minutes</th>
    </tr>
    %#for row in rows:

    <tr>
        <td>
        {{row[0]}}
        </td>
        <td>
        {{row[1]}}
        </td>
        <td>
        {{row[2]}}
        </td>
        <td>
        {{row[3]}}
        </td>
        <td>
        {{row[4]}}
        </td>
        <td>
        {{row[5]}}
        </td>
    </tr>
    %#end
</table>

