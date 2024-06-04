import React, { useState, useEffect } from 'react';
import { getTitles, generateAutoDocs } from './PythonStorybook';
import PrettyJsonDisplay from './PrettyStory'

export default {
    title: "Python/Example"
}

export const Welcome = () => {
    const [titles, setTitles] = useState([]);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        getTitles()
            .then(data => {
                setTitles(data.body); // API 응답에서 제목 목록 추출
                setIsLoading(false);
            })
            .catch(err => {
                setError(err.message);
                setIsLoading(false);
            });
    }, []); // 빈 배열을 전달하여 컴포넌트 마운트 시 한 번만 실행되도록 함

    if (isLoading) return <p>Loading...</p>;
    if (error) return <p>Error: {error}</p>;
    
    return (
        <div>
            <h1>Welcome to Story Hub</h1>
            <ul>
                {titles.map((title, index) => (
                    <li key={index}>{title}</li>
                ))}
            </ul>
        </div>
    );
}

export const GenerateDocumentation = () => {
    const [title, setTitle] = useState('');
    const [document, setDocument] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleTitleChange = (event) => {
        setTitle(event.target.value);
    };

    const handleGenerate = async () => {
        setIsLoading(true);
        setError(null);
        try {
            const docs = await generateAutoDocs(title);
            setDocument(docs); // 이 부분은 실제 API 응답 구조에 맞게 조정해야 함
            setIsLoading(false);
        } catch (err) {
            setError('Failed to generate documentation: ' + err.message);
            setIsLoading(false);
        }
    };

    return (
        <div>
            <h1>Generate Auto Documentation</h1>
            <input
                type="text"
                value={title}
                onChange={handleTitleChange}
                placeholder="Enter title for documentation"
            />
            <button onClick={handleGenerate} disabled={isLoading}>
                Generate
            </button>
            {isLoading && <p>Loading...</p>}
            {error && <p>{error}</p>}
            {document && <div><h2>Generated Documentation</h2>
            <PrettyJsonDisplay data={document.story_metas[0]} />
            <PrettyJsonDisplay data={document.story_metas[1]} />
            </div>}
        </div>
    );
}