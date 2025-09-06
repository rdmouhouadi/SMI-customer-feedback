# Smart Metering Feedback Portal  

*A lightweight Streamlit-based system for collecting customer feedback on smart metering solutions and visualizing insights in an analytics dashboard.*  

---

##### 🎯 Main Goals  
1. **Simplify customer feedback collection** through an interactive, user-friendly portal.  
2. **Ensure structured data capture** for multiple solution areas (e.g., WIZE, Endpoints, OGM, MDM).  
3. **Enable data-driven decisions** by analyzing satisfaction (SCAT score), sentiment, and raw responses.  

---

##### 💡 Why This Project  
Feedback from customers and partners is crucial for shaping the roadmap of smart metering solutions. This project was built to:  

- **Standardize Collection**: Replace unstructured forms and emails with a single feedback entry point.  
- **Improve Engagement**: Offer customers a smooth navigation experience with progress tracking across solution topics.  
- **Deliver Insights**: Provide internal stakeholders with a live analytics dashboard highlighting trends, satisfaction levels, and improvement areas.  

---

## 🛠️ Features  

**Current MVP Features**  
- Customer onboarding (name, email, company) with welcome & thank-you pages.  
- Topic-based questionnaire covering multiple solution areas.  
- Auto-save after each section submission, with completion tracking.  
- Navigation via sidebar and **Next / Previous** buttons.  
- Data persistence in CSV (ready for database integration).  

**Analytics Dashboard (in progress)**  
- Sidebar filters for slicing data (topic, company, time).  
- Computed **SCAT score** (satisfaction index).  
- **Sentiment analysis** of open-text responses.  
- Display of **raw responses table** linked to filters.  

**Possible Enhancements**  
- Authentication for customer-specific access.  
- Migration from CSV → SQL database.  
- Automated email confirmations or summaries.  
- Advanced analytics (topic modeling, trend analysis).  
- Deployment as a secure internal tool.  

---

## 🗺️ Roadmap  

### **Phase 1: MVP (POC)**  
- ✅ Build Streamlit form app for structured feedback collection.  
- ✅ Persist responses in CSV with timestamp + customer ID.  
- ✅ Add navigation and progress tracking.
- 🚧 Deploy the feedback portal (on Streamlit)
- 🚧 Build analytics dashboard with SCAT score + sentiment analysis.  

### **Phase 2: Scaling**  
- Migrate storage to SQL database.  
- Add Power BI or Streamlit dashboard with advanced filtering.  
- Automate sentiment scoring and satisfaction metrics.  

### **Phase 3: Deployment**  
- Deploy internally for Suez Smart Metering International team.  
- Add role-based access (customer vs. internal team).  
- Integrate advanced reporting (PDF export, email digest).  

---

## ⚡ Example Workflow  

1. **Customer** logs in with name, email, and company name.  
2. **Portal** displays feedback topics (WIZE, Endpoints, OGM, etc.) in the sidebar.  
3. **Customer** answers structured & open-ended questions per topic.  
4. **System** auto-saves responses after each section.  
5. **Dashboard** aggregates answers → shows SCAT (satisfaction) score, sentiment trends, and raw response tables.  
