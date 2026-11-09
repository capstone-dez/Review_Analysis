
import streamlit as st
import pandas as pd

# 1. 웹페이지 기본 설정
st.set_page_config(
    page_title="리뷰 분석 시스템",
    page_icon="📊",
    layout="wide"
)

# 2. 웹페이지 제목 및 설명
st.title("📊 리뷰 분석 시스템")
st.write("고객 리뷰 데이터를 분석하는 웹페이지입니다.")

st.divider()

# 3. CSV 파일 업로드
st.subheader("1. 리뷰 데이터 업로드")

uploaded_file = st.file_uploader(
    "CSV 파일을 선택하세요.",
    type=["csv"]
)

if uploaded_file is not None:

    try:
        # CSV 파일 읽기
        df = pd.read_csv(
            uploaded_file,
            encoding="utf-8-sig"
        )

        st.success("파일 업로드 성공!")

        # 별점 데이터를 숫자로 변환
        df["별점"] = pd.to_numeric(
            df["별점"],
            errors="coerce"
        )

        # 4. 기본 통계 분석
        st.subheader("2. 리뷰 기본 통계")

        total_reviews = len(df)
        avg_rating = df["별점"].mean()
        positive_reviews = (df["별점"] >= 4).sum()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("전체 리뷰 수", f"{total_reviews:,}건")

        with col2:
            st.metric(
                "평균 별점",
                f"{avg_rating:.2f}점" if pd.notna(avg_rating) else "데이터 없음"
            )

        with col3:
            st.metric("긍정 리뷰 수", f"{positive_reviews:,}건")

        # 5. 별점별 리뷰 현황
        st.subheader("3. 별점별 리뷰 현황")

        rating_count = (
            df["별점"]
            .value_counts()
            .sort_index()
        )

        st.bar_chart(rating_count)

        # 6. 전체 리뷰 데이터 출력
        st.subheader("4. 전체 리뷰 데이터")

        st.dataframe(
            df,
            use_container_width=True
        )

    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")

else:
    st.info("CSV 파일을 업로드해 주세요.")
