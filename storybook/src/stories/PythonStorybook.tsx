import axios from 'axios';

// Titles 타입 정의 (get_titles 응답에 맞춰서)
interface Titles {
    body: string[];
}

// AutoDocs 타입 정의 (generate_auto_docs 응답에 맞춰서)
interface AutoDocs {
    // 여기에 AutoDocs API 응답에 맞는 필드들을 추가
}

// get_titles API 호출
export const getTitles = async (): Promise<Titles> => {
    try {
        const response = await axios.get<Titles>('http://localhost:8000/get_titles', {
            headers: {
                accept: 'application/json',
            },
        });
        return response.data;
    } catch (error) {
        throw new Error('Failed to fetch titles');
    }
};

// generate_auto_docs API 호출
export const generateAutoDocs = async (title: string): Promise<AutoDocs> => {
    try {
        const response = await axios.post<AutoDocs>('http://localhost:8000/generate_auto_docs', {
            title: title
        }, {
            headers: {
                accept: 'application/json',
                'Content-Type': 'application/json',
            },
        });
        return response.data;
    } catch (error) {
        throw new Error('Failed to generate auto docs');
    }
};
