import axios from "axios"
import { useState } from "react"
import { useEffect } from "react"

const API = axios.create({
    baseURL: "http://127.0.0.1:5000",
    headers: { "Content-Type": "application/json" },
})

export default function TimeTable() {
    const times = [8,9,10,11,12,13,14]

    const days = ['', '일요일', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일']

    const [lectures, setLectures] = useState([]);
    const [students, setStudents] = useState([]);
    const [professors, setProfessors] = useState([]);
    const [type, setType] = useState([]);

    const getStudentLectures = async () => {
        try {
            const response = await API.get("/api/student_lecture_list/"+type[1])
            setLectures(response.data)
        } catch (e) {
            console.log(e)
        }
    }

    const getProfessorLectures = async () => {
        try {
            const response = await API.get("/api/professor_lecture_list/"+type[1])
            setLectures(response.data)
        } catch (e) {
            console.log(e)
        }
    }

    const getStudents = async () => {
        try {
            const response = await API.get("/api/student_list")
            setStudents(response.data)
        } catch (e) {
            console.log(e)
        }
    }

    const getProfessors = async () => {
        try {
            const response = await API.get("/api/professor_list")
            setProfessors(response.data)
        } catch (e) {
            console.log(e)
        }
    }

    useEffect(() => {
        getStudents()
        getProfessors()
    }, [])

    useEffect(() => {
        if(type[0] === "S") {
            getStudentLectures()
        }
        else if(type[0] === "P") {
            getProfessorLectures()
        }
    }, [type])

    useEffect(() => {
        days.forEach(day => {
            if(day !== "") {
                times.forEach(time => {
                    const block = document.getElementsByClassName(`${day} ${time}`)[0]
                    block.innerHTML = ""
                    block.style.backgroundColor = "aliceblue"
                    block.style.color = "black"
                    block.style.border = "1px solid black"
                    block.style.fontWeight = "normal"
                })
            }
        })
        lectures.map((lecture) => {
            for (let i = Number(lecture.start_time.split(':')[0]); i < Number(lecture.end_time.split(':')[0]); i++) {
                const block = document.getElementsByClassName(`${lecture.day} ${i}`)[0]
                block.innerHTML = `${lecture.course_name}<br/>[${lecture.professor_name}]`
                block.style.backgroundColor = "midnightblue"
                block.style.color = "white"
                block.style.border = "none"
                block.style.fontWeight = "bold"
            }
        })
    }, [lectures])

    return (
        <div>
            <table className="st">
                <thead>
                    <tr>
                        <th>
                            학생 시간표
                        </th>
                    </tr>
                </thead>
                <tbody>
                    {
                        students.map((student, index) => (
                            <tr key={index} onClick={() => setType(() => ["S", student.number])}>
                                <td>
                                    {student.number}
                                    &nbsp;
                                    {student.name}
                                </td>
                            </tr>
                        ))
                    }
                </tbody>
            </table>
            <table className="tt">
                <thead>
                    <tr>
                        <td colSpan={8}>
                            {type}
                        </td>
                    </tr>
                    <tr>
                        {
                            days.map((day, index) => (
                                <th key={index}>
                                    {day}
                                </th>
                            ))
                        }
                    </tr>
                </thead>
                <tbody>
                    {
                        times.map((time, index) => (
                            <tr key={index}>
                                {
                                    days.map((day, index) => (
                                        <td key={index} className={`${day} ${time}`}>
                                            {index === 0 && `${time-7}교시`}
                                        </td>
                                    ))
                                }
                            </tr>
                        ))
                    }
                </tbody>
            </table>
            <table className="st">
                <thead>
                    <tr>
                        <th>
                            교사 시간표
                        </th>
                    </tr>
                </thead>
                <tbody>
                    {
                        professors.map((professor, index) => (
                            <tr key={index} onClick={() => setType(() => ["P", professor.id])}>
                                <td>
                                    {professor.name}
                                    <br />
                                    [{professor.major}]
                                </td>
                            </tr>
                        ))
                    }
                </tbody>
            </table>
        </div>
    )
}